#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("Prueba")
        self.app.geometry("300x200")
        self.app.resizable(False, False)
        self.app.configure(bg="black")

        #Caja de texto donde aparecerá la información
        self.boxInfo = Text(self.app, width=40, height=10)
        self.boxInfo.pack(side="top")

        self.btnInfo = ttk.Button(self.app, text="Info", command=self.verinfo)
        self.btnInfo.pack(side="left")
        #self.btnInfo.focus_set()

        self.btnExit = ttk.Button(self.app, text="Exit", command=self.app.destroy)
        self.btnExit.pack(side="right")

        self.app.mainloop()

    def verinfo(self):
        #self.boxInfo.delete(0, END) #borra el contenido que haya en la caja de texto

        text = "'app' class: " + self.app.winfo_class() + "\n"
        text += "Class ID: " + str(self.app.winfo_id()) + "\n"
        text += "Application's width: " + str(self.app.winfo_width()) + "\n"
        text += "Application's height: " + str(self.app.winfo_height())

        self.boxInfo.insert(INSERT, text)


def main():
    app = Application()
    return 0

if __name__ == "__main__":
    main()
