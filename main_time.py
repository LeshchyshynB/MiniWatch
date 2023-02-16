from tkinter import *
from config import *

class Time():
    def __init__(self):

        self.create_struct()   

    def create_struct(self):
        s_x, s_y = 45, 120
        for i in range(0, 3):
            label_text[i].place(x=s_x, y=s_y, width=100, height=45)
            s_x += 80

        s_x, s_y = 45, 210
        for i in range(3, 5):
            label_text[i].place(x=s_x, y=s_y, width=100, height=45)
            s_x += 80
        label_text[5].place(x=225, y=s_y, width=100, height=45)

        s_x, s_y = 45, 50
        for i in range(0, 3):
            label_clock[i].place(x=s_x, y=s_y, width=100, height=100)
            s_x += 80

        s_x, s_y = 45, 140
        for i in range(3, 5):
            label_clock[i].place(x=s_x, y=s_y, width=100, height=100)
            s_x += 80
        label_clock[5].place(x=225, y=s_y, width=120, height=100)