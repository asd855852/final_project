import tkinter as tk
import time

import system
import api

from PIL import Image, ImageTk

#from darknet.darknet_video import yolo
labels = ['zhon','michael','boi']
class Clock(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg='black')
        
        self.clock = ''
        self.clockLabel = tk.Label(self, font=(
            'Helvetica', 90), fg="white", bg="black")
        self.clockLabel.pack(side=tk.TOP, anchor=tk.NE)
        
        self.day_of_week = ''
        self.dayOfWeekLabel = tk.Label(self, text=self.day_of_week, font=(
            'Helvetica', 45), fg="white", bg="black")
        self.dayOfWeekLabel.pack(side=tk.TOP, anchor=tk.NE)
        
        self.date = ''
        self.dateLabel = tk.Label(self, text=self.date, font=('Helvetica', 45), fg="white", bg="black")
        self.dateLabel.pack(side=tk.TOP, anchor=tk.NE)

        self.tick()
    
    def tick(self):
        day = system.nowDate()
        if day[0] != self.date:
            self.day_of_week = system.nowDate()[0]
            self.dayOfWeekLabel.config(text=self.day_of_week)
            self.date = system.nowDate()[1]
            self.dateLabel.config(text=self.date)
        self.clock = system.nowTime()
        self.clockLabel.config(text=system.nowTime())
        self.clockLabel.after(200, self.tick)

class Weather(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, bg='black')
        self.weather = ''
        self.weatherLabel = tk.Label(self, text=self.weather, font=(
            'Helvetica', 45), fg="white", bg="black")
        self.weatherLabel.pack(side=tk.TOP, anchor=tk.W)

        self.weatherIcon = ''
        self.weatherIconLabel = tk.Label(self, fg="white", bg="black")
        self.weatherIconLabel.pack(side=tk.TOP, anchor=tk.N, padx=20)

        self.temp = ''
        self.tempLabel = tk.Label(self, text=self.temp, font=(
            'Helvetica', 45), fg="white", bg="black")
        self.tempLabel.pack(side=tk.LEFT, anchor=tk.W)

        self.setWeather()
    
    def setWeather(self):
        self.data = system.getWeather()
        self.weatherLabel.config(text=self.data[0])
        self.tempLabel.config(text=self.data[1])
        self.weatherIconLabel.config(image=self.data[2])
        self.weatherIconLabel.image = self.data[2]

        # 3小時更新一次
        self.weatherLabel.after(10000000, self.setWeather)
    
    def ReloadWeather(self):
        self.data = system.getWeather()
        self.weatherLabel.config(text=self.data[0])
        self.tempLabel.config(text=self.data[1])
        self.weatherIconLabel.config(image=self.data[2])
        self.weatherIconLabel.image = self.data[2]

class News(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='black')
        data=api.getNews(system.settings['country'])
        self.length = len(data['articles'])
        if(self.length>10):
            self.length=10
        self.titleLabel=[]
        for i in range(self.length):
            self.titleLabel.append(tk.Label(self, font=('Helvetica', 16), fg="white", bg="black"))
            self.titleLabel[i].pack(side=tk.BOTTOM,anchor=tk.W)
            self.setNews(i)
    def setNews(self,i):
        self.news_data = api.getNews(system.settings['country'])
        self.titleLabel[i].config(text=self.news_data['articles'][i].get("title"))

        # 1小時更新一次
        self.titleLabel[i].after(3600000, self.setNews)
    
    def ReloadNews(self):
        self.news_data=api.getNews(system.settings['country'])
        for i in range(self.length):
            self.titleLabel[i].config(text=self.news_data['articles'][i].get("title"))
count = 0

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='#000000')
        self.window.attributes('-fullscreen', True)
        # user
#        self.buttonChangeUser=tk.Button(self.window,text='Change User',activebackground='black',activeforeground='yellow',command=self.changeUser)
#        self.buttonChangeUser.pack(side=tk.BOTTOM, anchor=tk.SE)
#        self.ClientLabel=tk.Label(self.window,text="Hi! "+system.settings['name'],font=('Helvetica', 16), fg="white", bg="black")
#        self.ClientLabel.pack(side=tk.BOTTOM, anchor=tk.SE)
        self.img=Image.open(system.settings['icon'])
        self.userIcon=ImageTk.PhotoImage(self.img)
        #self.panel=tk.Label(self.topFrame, image=self.userIcon)
        # self.panel.pack(side=tk.RIGHT, anchor=tk.SE)
        # self.userIcon.pack(side=tk.BOTTOM, anchor=tk.E)
        # window
        self.topFrame = tk.Frame(self.window, background= '#000000')
        self.topFrame.pack(side=tk.TOP, fill=tk.BOTH)
        self.bottomFrame = tk.Frame(self.window, background= '#000000')
        self.bottomFrame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        # self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=tk.RIGHT, anchor=tk.NE)
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=tk.LEFT, anchor=tk.NW)
        # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=tk.LEFT, anchor=tk.SW)
        # user
        self.buttonChangeUser=tk.Button(self.bottomFrame,text='Change User',activebackground='black',activeforeground='yellow',command=self.changeUser)
        self.buttonChangeUser.pack(side=tk.BOTTOM, anchor=tk.SE)
        self.ClientLabel=tk.Label(self.bottomFrame,text="Hi! "+system.settings['name'],font=('Helvetica', 16), fg="white", bg="black")
        self.ClientLabel.pack(side=tk.BOTTOM, anchor=tk.SE)
        self.panel=tk.Label(self.bottomFrame, image=self.userIcon)
        self.panel.pack(side=tk.BOTTOM, anchor=tk.NE)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def changeUser(self):
        global count
        count += 1
        count %= 3  
#        try:
#           print("count: "+str(count))
#            if(count==0):
        labels = ['zhon','michael','boi']
  #          count+=1
   #         if(count>=2):
    #            count=0
        print("in change User-------------------------------------------")
        print(labels)
 #       except Exception as e:
  #          print(e)
        if(labels[count]=='zhon'):
            system.settings['name']='zhon'
            system.settings['lang']='tw-ch'
            system.settings['location']='Taiwan, TW'
            system.settings['country']='tw'
            system.settings['icon']='./user/zhon.jpg'
        elif (labels[count]=='michael'):
            system.settings['name']='michael'
            system.settings['lang']='en'
            system.settings['location']='New York City, US'
            system.settings['country']='ng'
            system.settings['icon']='./user/michael.jpg'
        elif (labels[count]=='boi'):
            system.settings['name']='boi'
            system.settings['lang']='ja'
            system.settings['location']='Yokohama, JP'
            system.settings['country']='jp'
            system.settings['icon']='./user/boi.jpg'

        self.panel.destroy()
        self.img=Image.open(system.settings['icon'])
        self.userIcon=ImageTk.PhotoImage(self.img)
        self.panel=tk.Label(self.bottomFrame, image=self.userIcon)
        self.panel.pack(side=tk.BOTTOM, anchor=tk.NE)
        self.ClientLabel.config(text="Hi! "+system.settings['name'])
        self.news.ReloadNews()
        self.weather.ReloadWeather()
        print(system.settings)
        self.window.update_idletasks()

if __name__ == '__main__':
    w = Window()
    w.window.mainloop()
