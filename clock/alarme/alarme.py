from cgitb import text
from tkinter import *
from time import localtime 
from pygame import mixer


def alarm():
    hora = int(input('Digite a hora: '))
    minuto = int(input('Digite o minuto: '))

    while True:
        if localtime().tm_hour == hora and localtime().tm_min == minuto:
            print('HORA DE ACORDAR')
            mixer.init()
            mixer.music.load("endereço do arquivo")
            mixer.music.play()
        break

janela = Tk()
janela.title('Alarme')

texto = Label(janela, text='Clique no botão para acertar o alarme')
texto.grid(column=0, row=0)


texto_orientacao1 = Label(janela, text='hora: ')
texto_orientacao1.grid(column=0, row=1)

texto_orientacao2 = Label(janela, text='minuto: ')
texto_orientacao2.grid(column=0, row=1)

botao = Button(janela, text='Digite a hora', command=alarm)
botao.grid(column=0, row=1)

botao = Button(janela, text='Digite o minuto', command=alarm)
botao.grid(column=0, row=2)

texto_alarme = Label(janela, text='')

janela.mainloop()