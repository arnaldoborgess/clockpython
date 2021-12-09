import tkinter as tk
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') # -*- coding: utf-8 -*-

class TelaPrincipal:
    def __init__(self, master):
        self.tela = master
        self.relogio_digital = tk.Label(
        self.tela, font=('LCDMono2', 26), fg='white', bg = 'black')
        self.relogio_digital.pack(pady=0, padx=0)
        self.hora()

    def hora(self):
        agora = datetime.datetime.now()
        self.relogio_digital['text'] = agora.strftime('%A, %d %B %Y\n%H:%M:%S')
        self.tela.after(1000, self.hora)

janela_raiz = tk.Tk()
TelaPrincipal(janela_raiz)
janela_raiz.mainloop() 
