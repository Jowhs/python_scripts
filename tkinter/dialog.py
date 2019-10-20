#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

class Application():
    window = 0
    posx_y = 0

    def __init__(self):
        self.app = Tk()
        self.app.geometry("300x200+500+50")
        self.app.resizable(False, False)
        self.app.title("Main Window")

        btn = ttk.Button(self.app, text="Open", command=self.open)
        btn.pack(side="bottom", padx=20, pady=20)

        self.app.mainloop()

    def open(self):
        self.dialog = Toplevel()
        Application.window += 1

        #Application.posx_y += 400
        sizepos = "200x100+750+250" #+ str(Application.posx_y) + "+" +str(Application.posx_y)

        self.dialog.geometry(sizepos)
        self.dialog.resizable(False, False)

        #nid = self.dialog.winfo_id() # Obtenemos un nuevo ID para crear un título para la nueva ventana
        #ntit = str(Application.window) + ": " + str(nid)
        self.dialog.title("Dialog")

        btnClose = ttk.Button(self.dialog, text="Close", command=self.dialog.destroy)
        btnClose.pack(side="bottom", padx=20, pady=20)

        self.app.wait_window(self.dialog)

def main():
    app = Application()
    return 0

if __name__ == "__main__":
    main()
