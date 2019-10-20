import socket
from tkinter import ttk
from tkinter import *

class Connection:

    def __init__(self, window):
        self.wind = window
        self.wind.title("TSStrojan")

        fr = Label(self.wind, text = "Connect with host")
        fr.grid(row = 0, column = 0, pady = 20, padx = 20)

        Label(fr, text = "Name: ").grid(row = 1, column = 0, pady = 20, padx = 20)


        #btn = ttk.Button(fr, text = "Connect")
        #btn.grid(row = 1, column = 0)






if __name__ == "__main__":
    window = Tk()
    application = Connection(window)
    window.mainloop()
