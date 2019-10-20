#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass

class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("Access")

        self.app.geometry("400x300")
        self.app.resizable(False, False)

        self.fnt = font.Font(weight="bold")

        self.tag1 = ttk.Label(self.app, text="User: ", font=self.fnt)
        self.tag2 = ttk.Label(self.app, text="Password: ", font=self.fnt)

        self.msg = StringVar()
        self.tag3 = ttk.Label(self.app, textvariable=self.msg, font=self.fnt, foreground="blue")

        self.user = StringVar()
        self.passwd = StringVar()

        self.user.set(getpass.getuser())

        self.fieldUser = ttk.Entry(self.app, textvariable=self.user, width=30)
        self.fieldPasswd = ttk.Entry(self.app, textvariable=self.passwd, width=30, show="*")
        self.sep = ttk.Separator(self.app, orient="horizontal")

        self.btnAccept = ttk.Button(self.app, text="Login", command=self.login)
        self.btnCancel = ttk.Button(self.app, text="Cancel", command=quit)

        self.tag1.place(x=25, y=40)
        self.fieldUser.place(x=130, y=40)
        self.tag2.place(x=25, y=80)
        self.fieldPasswd.place(x=130, y=80)
        self.tag3.place(x=150, y=100)
        self.btnAccept.place(x=150, y=120)
        self.btnCancel.place(x=270, y=120)

        self.fieldPasswd.focus_set()

        self.fieldPasswd.bind("<Button-1>", self.delete_msg)

        self.app.mainloop()

    def login(self):
        if self.passwd.get() == 'tkinter':
            self.tag3.configure(foreground="blue")
            self.msg.set("You are logged in")
        else:
            self.tag3.configure(foreground="red")
            self.msg.set("Access denied")

    def delete_msg(self, event):
        self.passwd.set("")
        self.msg.set("")

def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()
