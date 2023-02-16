from config import Config
from config import *

class Stopwatch_init():
    def __init__(self):
        for i in range(4):
            label=Label(window, font=("Futura PT", 40), fg="White", bg = "Black", text="00")
            label_stopwatch.append(label)

        btn_start = Button(text='Start',font=("Futura PT", 10),fg="White",bg = "Black",command=Config.update_stopwatch)
        btn_stop = Button(text='Stop',font=("Futura PT", 10),fg="White",bg = "Black",command=Config.stop_update_stopwatch)
        btn_stopwatch.append(btn_start)
        btn_stopwatch.append(btn_stop)