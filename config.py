from tkinter import *
from time import strftime, sleep, time

window = Tk()
window.title("Watch")
window.resizable(False, False)
window.geometry("350x300")
window["bg"] = "black"

label_clock=[]
label_text=[]

label_stopwatch=[]
btn_stopwatch=[]

class Config():
    def __init__(self):
        self.btn1=Button(text='Watch', font=("Futura PT", 10), fg="White", bg = "Black",command=self.watch)
        self.btn2=Button(text='StopWatch', font=("Futura PT", 10), fg="White", bg = "Black",command=self.stopwatch)
        self.btn3=Button(text='Timer', font=("Futura PT", 10), fg="White", bg = "Black")

    def update_clock(self):
        h = strftime("%H")
        m = strftime("%M")
        s = strftime("%S")
        d = strftime("%d")
        mo = strftime("%m")
        y = strftime("%Y")
        try:
            label_clock[0].config(text="{}".format(h))
            label_clock[1].config(text="{}".format(m))
            label_clock[2].config(text="{}".format(s))
            label_clock[3].config(text="{}".format(d))
            label_clock[4].config(text="{}".format(mo))
            label_clock[5].config(text="{}".format(y))
        except:
            pass

        window.after(1000, self.update_clock)

    def update_stopwatch(self):
        print("1")

        window.after(1000, self.update_stopwatch)

    def stop_update_stopwatch(self):
        window.after_cancel(window)