# 投籃數據分析
使用簡單的頁面記錄投籃數據，並輸出計算命中率，收集一段時間的數據後，開始分析這一段時間內此數據的命中率趨勢，從中觀察此球員的命中率穩定度如何、團隊中哪位球員的命中率最穩定等
## 使用工具
HTML/CSS/JavaScript/python/SQL資料庫
## 架構
首先利用到Python的flask套件，通常會有 app.py 跟 template、static 兩個資料夾
* static 用來放 css 和 js 檔
* template 用來放 html 檔

<img src="image/i_1.png" width="300" height="500" alt="Image">


### **app.py** 
是 Flask 應用程式的核心，其中包含了應用程式的主要配置和邏輯，並負責啟動整個應用。

<img src="image/i_2.png" width="600" height="600" alt="Image">

引入 Python 內建的 sqlite3 模組，之後將會使用到 SQLite3 資料庫，接著定義一個處理根路徑的函式，當用戶訪問網站時，會進入 'index.html' 的模板檔案。最後連接了一個 SQLite3 資料庫的函式，確保在使用資料庫時能正確地建立連線。


## 對數頻譜分析

對數頻譜可以洞察信號處理後的頻率組分。圖3和圖4描繪了兩個音頻通道的對數頻譜：


對數頻譜應該在濾波器通帶外的頻率顯示一條平線，這表明濾波器有效地衰減了這些頻率：

1. **濾波結果**：如果對數頻譜在濾波器的通帶外顯示了一條平線，則表明濾波器有效地衰減了那些頻率。
2. **驗證正確性**：要證明對數頻譜顯示了正確的濾波結果，可以將這些結果與濾波器的理論響應進行比較。實際結果應該與基於濾波器設計的
