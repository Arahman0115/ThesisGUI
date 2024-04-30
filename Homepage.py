from tkinter import *

def HomePage(self):
    self.hide_frames()
    self.Rx_homepage.pack()

    swidth = self.winfo_width()
    sheight = self.winfo_height()
    self.Mainprod3 = Canvas(self.Rx_homepage, width=swidth, height=sheight, bg='blue', relief=SUNKEN, borderwidth=5)
    self.Mainprod3.pack()
    self.Mainprod3.create_text(40, 20, text='Welcome!', fill="black", font=('Trajan Pro', 13, 'bold'))
