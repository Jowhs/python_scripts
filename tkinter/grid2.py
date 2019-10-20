#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("Access")

        fnt = font.Font(weight="bold")

        self.fr = ttk.Frame(self.app, borderwidth=4, relief="raised", padding=(10,10))

        self.tag1 = ttk.Label(self.fr, text="User: ", font=fnt)
        self.tag2 = ttk.Label(self.fr, text="Password: ", font=fnt)

        self.user = StringVar()
        self.passwd = StringVar()

        self.user.set(getpass.getuser())

        self.fieldUser = ttk.Entry(self.fr, textvariable=self.user, width=30)
        self.fieldPasswd = ttk.Entry(self.fr, textvariable=self.passwd, width=30, show="*")
        self.sep = ttk.Separator(self.fr, orient="horizontal")

        self.btnLogin = ttk.Button(self.fr, text="Login", command=self.login)
        self.btnCancel = ttk.Button(self.fr, text="Cancel", command=quit)

        self.fr.grid(row=0, column=0, sticky=(N,S,E,W))
        self.tag1.grid(row=0, column=0, sticky=(N,S,E,W))
        self.fieldUser.grid(row=0, column=1, columnspan=2)
        self.tag2.grid(row=1, column=0, pady=10)
        self.fieldPasswd.grid(row=1, column=1, columnspan=2)
        self.btnLogin.grid(row=4, column=1)
        self.btnCancel.grid(row=4, column=2)

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.fr.columnconfigure(0, weight=1)
        self.fr.columnconfigure(1, weight=1)
        self.fr.columnconfigure(2, weight=1)
        self.fr.rowconfigure(0, weight=1)
        self.fr.rowconfigure(1, weight=1)
        self.fr.rowconfigure(4, weight=1)

        self.fieldPasswd.focus_set()

        self.app.mainloop()

    def login(self):
        if self.passwd.get() == 'tkinter':
            print("You are logged in")
            print("User: ", self.fieldUser.get())
            print("Password: ", self.fieldPasswd.get())
        else:
            print("Access denied")
            self.passwd.set("")
            self.fieldPasswd.focus_set()

def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()
