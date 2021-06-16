# Smart Mirror智能鏡子
搭配單面透鏡，以達到鏡子的效果，會在螢幕上顯示時間
以及由Weather API和News API獲取資訊
且有更換使用者的按鍵，按下後變更使用者頭像和名稱還會根據設定的使用者更換國家而改變獲取的資料，改變成當地國家的天氣和新聞。

# 功能

鏡面下顯示介面主要由
Python Tkinter設計與規劃，因為盡量保留鏡子的特性，因此在介面的規劃上面並沒有添加太多資訊，讓使用者
仍保有大面積鏡面的區域。主程式為 main.py 主要做整體介面的規
劃，如：左上角的部分顯示當前當地的天氣概況；右上角則顯示日期
與時間；左下角顯示當前當地的新聞；以及右下角的當前使用者與使
用者切換按鍵。  
所使用的API則編寫在api.py裡面:天氣概況透過
OpenWeatherAPI取得；新聞資訊則透過newsapi.org。 
在右下角則會顯示設定好的使用者，其中的設定的資訊包括:使用者名稱、頭像、國家還有語言。
並且提供更換使用者按鍵，可以進行使用者的切換，方便提供多位使用者使用，切換後也會根據使用者的地區、語言，更新成該地區的適合的介面。
![image](https://github.com/asd855852/final_project/blob/main/final1.PNG)
![image](https://github.com/asd855852/final_project/blob/main/final2.PNG)
![image](https://github.com/asd855852/final_project/blob/main/final3.PNG)  
當系統開機時，便會 執行 main.py中 的 tick(), setWeather()以及
執行預設設定的介面。使用者可以藉由鏡面下的顯示器，取得一些重要的資訊以及在右下角的部分會顯示當前的使用者。在鏡面的右
下角可以透過Change User的按鍵做使用者的切換，當按下按鍵時將下一位使用者傳回至main.py做ReloadNews(),ReloadWeather()介面的刷新。
# 參考資料
Magic Mirror for JavaScript: https://github.com/MichMich/MagicMirror  
Python Tkinter: https://docs.python.org/3/library/tkinter.html  
Weather API: https://openweathermap.org/api  
News API: https://newsapi.org  

# 安裝
在python環境下  
以cmd
先安裝Pillow   
`pip install pillow`  
再安裝feedparser  
`pip install feedparser`  
並在存放檔案的目錄下執行main.py  
`python main.py`
