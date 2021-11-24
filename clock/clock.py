import tkinter as tk
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') # -*- coding: utf-8 -*-

class TelaPrincipal:
    def __init__(self, master):
        self.tela = master
        self.relogiodigital = tk.Label(
        self.tela, font=('Arial', 26), fg='green', bg = 'Black')
        self.relogiodigital.pack(pady=30, padx=30)
        self.hora()

    def hora(self):
        agora = datetime.datetime.now()
        self.relogiodigital['text'] = agora.strftime('%A, %d %B %Y\n%H:%M:%S')
        self.tela.after(1000, self.hora)

janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop() # bloqueia qualquer código até que a janela seja fechada
