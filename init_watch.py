from config import Config
from config import *

class Watch_init():
    def __init__(self):
        for i in range(6):
            label = Label(window, font=("Futura PT", 40), fg="White", bg = "Black", text="00")
            label_clock.append(label)

        for i in range(6):
            label = Label(window, font=("Futura PT", 20), fg="White", bg = "Black", text="Hou")
            label_text.append(label)
        label_text[1].config(text="Min")
        label_text[2].config(text="Sec")
        label_text[3].config(text="Day")
        label_text[4].config(text="Mou")
        label_text[5].config(text="Year")