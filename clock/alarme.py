from time import localtime #  permite que o código leia a hora e o minuto do computador.
from pygame import mixer # permite que o código leia arquivos de mídia


hora = int(input('Coloque a Hora: ')) # entrar com o valor da hora
minuto = int(input('Coloque o Minuto: ')) # entrar com o valor do minuto

while True:
    if localtime().tm_hour == hora and localtime().tm_min == minuto:
        print('HORA DE ACORDAR')
        mixer.init()
        mixer.music.load("endereço do arquivo")
        mixer.music.play()
    break