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

        self.tag1 = ttk.Label(self.app, text="User: ", font=fnt)
        self.tag2 = ttk.Label(self.app, text="Password: ", font=fnt)

        self.user = StringVar()
        self.passwd = StringVar()

        self.user.set(getpass.getuser())

        self.fieldUser = ttk.Entry(self.app, textvariable=self.user, width=30)
        self.fieldPasswd = ttk.Entry(self.app, textvariable=self.passwd, width=30, show="*")
        self.sep = ttk.Separator(self.app, orient="horizontal")

        self.btnAccept = ttk.Button(self.app, text="Login", command=self.login)
        self.btnCancel = ttk.Button(self.app, text="Cancel", command=quit)

        self.tag1.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        self.fieldUser.pack(side="top", fill="x", expand=True, padx=5, pady=5)
        self.tag2.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        self.fieldPasswd.pack(side="top", fill="x", expand=True, padx=5, pady=5)
        self.btnAccept.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.btnCancel.pack(side="right", fill="both", expand=True, padx=5, pady=5)

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
