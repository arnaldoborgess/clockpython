from time import localtime 
from pygame import mixer

hora = int(input('Coloque a Hora: ')) # entrar com o valor da hora
minuto = int(input('Coloque o Minuto: ')) # entrar com o valor do minuto

while True:
    if localtime().tm_hour == hora and localtime().tm_min == minuto:
        print('HORA DE ACORDAR')
        mixer.init()
        mixer.music.load("endereço do arquivo")
        mixer.music.play()
    break