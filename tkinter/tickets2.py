#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

class Application():
    def __init__(self):
        self.app = Tk()
        self.app.title("Travel")
        self.app.geometry("350x650")
        self.app.resizable(False, False)

        self.travelers_num = IntVar()
        self.gone_back = BooleanVar()
        self.cls = StringVar(value="t")
        self.km = IntVar(value=1)
        self.price = DoubleVar(value=0.10)
        self.total = DoubleVar(value=0.0)

        # Al definir trazas con variables de control de los 'Entry'
        # podemos detectar cambios y llamar a la función self.Calculate
        # para que lo valide y calcule al instante

        self.km.trace('w', self.calculate)
        self.price.trace('w', self.calculate)

        self.calculate()

        # En esta ocasión utilizaremos 'command' en los Spinbox, Checkbutton
        # y Radiobutton para validación y calculo inmediato

        #-----Imagen del tren-----#
        train = PhotoImage(file="tren.gif")
        self.image = ttk.Label(self.app, image=train, anchor="center")
        #------------------
        self.tag_trav = ttk.Label(self.app, text="Travelers: ")
        self.num = Spinbox(self.app, from_=1, to=20, wrap=True, textvariable=self.travelers_num, state="readonly", command=self.calculate)
        self.round = ttk.Checkbutton(self.app, text="Round Trip", variable=self.gone_back, onvalue=True, offvalue=False, command=self.calculate)
        #------------------
        self.tag_cls = ttk.Label(self.app, text="Class: ")
        self.cls1 = ttk.Radiobutton(self.app, text="Tourist", variable=self.cls, value="t", command=self.calculate)
        self.cls2 = ttk.Radiobutton(self.app, text="First", variable=self.cls, value="f", command=self.calculate)
        self.cls3 = ttk.Radiobutton(self.app, text="Lux", variable=self.cls, value="l", command=self.calculate)
        #------------------
        self.tag_km = ttk.Label(self.app, text="Distance (Km): ")
        self.dist = ttk.Entry(self.app, textvariable=self.km, width=10)
        #------------------
        self.tag_price = ttk.Label(self.app, text="Price: ")
        self.cost = ttk.Entry(self.app, textvariable=self.price, width=10)
        self.tag_pay = ttk.Label(self.app, text="Total: ")
        #cambiar foreground y background por fg y bg respectivamente, borderwidth por bd
        self.screen_pay = ttk.Label(self.app, textvariable=self.total, foreground="yellow", background="black", borderwidth=5, anchor="e")
        self.separator = ttk.Separator(self.app, orient=HORIZONTAL)
        #------------------
        self.btn_calc = ttk.Button(self.app, text="Calculate", command=self.calculate)
        self.btn_exit = ttk.Button(self.app, text="Exit", command=quit)

        #-----Posicionamiento elementos-----#

        self.image.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.tag_trav.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.num.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.round.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.tag_cls.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.cls1.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.cls2.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.cls3.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.tag_km.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.dist.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.tag_price.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.cost.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.tag_pay.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.screen_pay.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.separator.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.btn_calc.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.btn_exit.pack(side=RIGHT, fill=BOTH, expand=True,  padx=10, pady=10)

        self.app.mainloop()

    def calculate(self, *args):
        data_error = False
        total = 0
        try:
            km = int(self.km.get())
            price = float(self.price.get())
        except:
            data_error = True

        if not data_error:
            total = self.travelers_num.get() * km * price
            if self.gone_back.get():
                total = total * 1.5
            if self.cls.get() == 'f':
                total = total * 1.2
            elif self.cls.get() == 'l':
                total = total * 2
            self.total.set(total)
        else:
            self.total.set("ERROR!")


def main():
    app = Application()
    return 0

if __name__ == '__main__':
    main()
