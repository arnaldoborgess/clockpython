import tkinter as tk
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') # -*- coding: utf-8 -*-
#locale.setlocale(locale.LC_ALL, 'en_ZW.utf8')

class TelaPrincipal:
    def __init__(self, master):
        self.tela = master
        self.relogiodigital = tk.Label(
            self.tela, font=('Arial', 26), fg='green', bg = 'Black')
        self.relogiodigital.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        #now = datetime.datetime.now()
        agora = datetime.datetime.now()
        #self.relogiodigital['text'] = agora.strftime('%c')
        self.relogiodigital['text'] = agora.strftime('%A, %d %B %Y\n%H:%M:%S')
        self.tela.after(1000, self.alteracao)

janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop() # bloqueia qualquer código até que a janela seja fechada
