from tkinter import *
from config import *

class Destroy_widgets():
    def __init__(self):
        window.after_cancel(window)
        all_widgets = [label_clock, label_text]
        for i in all_widgets:
            for j in i:
                j.place_forget()
            i.clear()