from tkinter import *

class HomeScreen(Frame):

    def __init__(self, width, height, title):
        Frame.__init__(self, master=None)
        self.master.title(title)
        self.set_geometry(width, height)


    def set_geometry(self, width, height):
        positionRight = int(self.master.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.master.winfo_screenheight() / 2 - height / 2)
        self.master.geometry("{}x{}+{}+{}".format(width, height, positionRight, positionDown))