# -*- coding: utf-8 -*-
import tkinter as tk
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('Arial', 26), fg='Black')
        self.lblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()
        
        self.lblRelogio['text'] = now.strftime('%A, %d %B %Y\n%H:%M:%S')

        self.nossaTela.after(1000, self.alteracao)


janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()
