"""次中音薩克斯風練習室：Streamlit Community Cloud 版本。

把 tenor-sax-practice.html 原封不動地放進一個 iframe 執行。
- 錄音樣本 samples/builtin.json 直接嵌進頁面（不靠 fetch），本機與雲端都能用。
- 進度存在瀏覽器的 localStorage（離開 claude.ai 後頁面會自動改用本機儲存）。
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent
PAGE = HERE / "tenor-sax-practice.html"
SAMPLES = HERE / "samples" / "builtin.json"

# 頁面原本用 fetch 讀樣本；改成先找嵌入的 <script id="builtin-samples">，找不到才 fetch。
FETCH_OLD = 'const res = await fetch("samples/builtin.json"); if (!res.ok) return;'
FETCH_NEW = (
    'const el = document.getElementById("builtin-samples"); '
    'const res = el ? null : await fetch("samples/builtin.json"); '
    'if (!el && !res.ok) return;'
)
PARSE_OLD = "const j = await res.json();"
PARSE_NEW = "const j = el ? JSON.parse(el.textContent) : await res.json();"

st.set_page_config(
    page_title="次中音薩克斯風練習室",
    page_icon="🎷",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_resource(show_spinner="載入練習頁與錄音樣本…")
def build_page() -> str:
    html = PAGE.read_text(encoding="utf-8")
    for old, new in ((FETCH_OLD, FETCH_NEW), (PARSE_OLD, PARSE_NEW)):
        if html.count(old) != 1:
            raise RuntimeError(f"練習頁的程式碼和預期不同，找不到：{old}")
        html = html.replace(old, new)

    samples = SAMPLES.read_text(encoding="utf-8") if SAMPLES.exists() else ""
    if "</script" in samples.lower():
        raise RuntimeError("builtin.json 含有 </script>，不能直接嵌入頁面")
    embed = (
        f'<script type="application/json" id="builtin-samples">{samples}</script>'
        if samples
        else ""
    )

    # 練習頁原本由 claude.ai 補上 doctype 與 head，這裡自己補。
    return (
        "<!doctype html><html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<style>html,body{margin:0}</style></head><body>"
        f"{embed}{html}</body></html>"
    )


# 縮小 Streamlit 自己的外框留白，讓練習頁佔滿畫面。
st.markdown(
    """
    <style>
      .block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 100%;}
      header[data-testid="stHeader"] {height: 0; min-height: 0;}
      footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("顯示設定")
    height = st.slider("練習頁高度（像素）", 1200, 6000, 3400, step=200,
                       help="頁面下方被切掉時調高；手機上覺得太長可以調低。")
    st.caption(
        "錄音：Good-sounds 資料集（MTG, Universitat Pompeu Fabra），"
        "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。"
        "練習進度只存在這台裝置的瀏覽器裡，換裝置或清除瀏覽資料就會不見。"
    )

try:
    page = build_page()
except (OSError, RuntimeError) as err:
    st.error(f"練習頁載入失敗：{err}")
    st.stop()

components.html(page, height=height, scrolling=True)
