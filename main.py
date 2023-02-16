from tkinter import *
from time import strftime, sleep, time
from main_time import Time
from main_stopwatch import Stopwatch
#from main_timer import Timer
from config import *
from clear_all import Destroy_widgets
from config import Config
from init_main import Init


class Watch(Config):
    def __init__(self):
        super().__init__()
        self.btn1.place(x=0,y=0,width=100,height=30)
        self.btn2.place(x=100,y=0,width=100,height=30)
        self.btn3.place(x=200,y=0,width=100,height=30)

        self.watch()
        
        window.mainloop()


    def watch(self):
        Destroy_widgets()
        Init.watch()
        Time()
        self.update_clock()
        

    def stopwatch(self):
        Destroy_widgets()
        Init.stopwatch()
        Stopwatch()


    def timer(self):
        Destroy_widgets()
        Init.timer()
        #Timer()


if __name__ == "__main__":
    Watch()