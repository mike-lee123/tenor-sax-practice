# 次中音薩克斯風練習室（Streamlit 版）

B♭ 次中音薩克斯風的課程、樂譜庫、指法圖與真實錄音示範。

## 檔案

```
app.py                     Streamlit 主程式
requirements.txt           套件清單
.streamlit/config.toml     Streamlit 設定
tenor-sax-practice.html    練習頁本體
samples/builtin.json       次中音錄音樣本（約 6 MB）
```

## 本機試跑

```
pip install -r requirements.txt
streamlit run app.py
```

瀏覽器會打開 http://localhost:8501 。

## 部署到 Streamlit Community Cloud（免費）

1. **建立 GitHub 儲存庫**：登入 https://github.com ，按右上角「+」→「New repository」，名稱例如 `tenor-sax-practice`，選 Public，按「Create repository」。
2. **上傳檔案**：在新儲存庫頁面按「uploading an existing file」，把這個資料夾裡的**全部內容**（包含 `.streamlit` 和 `samples` 兩個資料夾）拖進去，按「Commit changes」。上傳後確認儲存庫裡看得到 `.streamlit/config.toml` 和 `samples/builtin.json`。
3. **建立 App**：到 https://share.streamlit.io ，用 GitHub 帳號登入，按「Create app」→「Deploy a public app from GitHub」。
   - Repository：選剛才的儲存庫
   - Branch：`main`
   - Main file path：`app.py`
   - App URL：可以自訂，例如 `tenor-sax-practice`，網址就是 `https://tenor-sax-practice.streamlit.app`
4. 按「Deploy」，等一兩分鐘第一次安裝完成，就會得到固定網址。

## 之後要更新

在 GitHub 儲存庫裡直接修改或重新上傳 `tenor-sax-practice.html`（或 `samples/builtin.json`），Streamlit Cloud 會自動重新部署，網址不變。

## 注意

- **休眠**：免費方案的 App 一段時間沒人使用會進入休眠，打開時會看到喚醒按鈕，按下去等幾十秒就能用。網址本身不會變。
- **練習進度**：存在每台裝置的瀏覽器裡（localStorage）。換手機、換瀏覽器或清除瀏覽資料，進度就不會跟過去；也不會和 claude.ai 版本的進度同步。
- **頁面高度**：練習頁放在固定高度的框裡。下方被切掉時，打開左側欄調整「練習頁高度」。
- **公開儲存庫**：Public 儲存庫的檔案任何人都看得到。內容只有練習頁與錄音樣本，沒有個人資料。
- **錄音授權**：錄音來自 Good-sounds 資料集（Music Technology Group, Universitat Pompeu Fabra），依 CC BY 4.0 使用；頁面頁尾和側欄的出處說明請保留。
