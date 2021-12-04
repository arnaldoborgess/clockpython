from time import localtime 
from pygame import mixer

hora = int(input('Coloque a Hora: '))
minuto = int(input('Coloque o Minuto: '))

while True:
    if localtime().tm_hour == hora and localtime().tm_min == minuto:
        print('HORA DE ACORDAR')
        mixer.init()
        mixer.music.load("endereço do arquivo")
        mixer.music.play()
    break