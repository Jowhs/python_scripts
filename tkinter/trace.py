#!/usr/bin/python3
# -*- coding: utf-8 -*-

def cambia(*args):
    print("Ha cambiado su valor")

def lee(*args):
    print("Ha sido leido su valor")

variable = StringVar()
variable.trace("w", cambia)
variable.trace("r", lee)
variable.set("Hola")
print(variable.get())
print(variable.get())
