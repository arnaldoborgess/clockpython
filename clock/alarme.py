from time import localtime 
from pygame import mixer

def alarm():
    hora = int(input('Digite a hora: '))
    minuto = int(input('Digite o minuto: '))

    while True:
        if localtime().tm_hour == hora and localtime().tm_min == minuto:
            print('HORA DE ACORDAR')
            mixer.init()
            mixer.music.load("play.wav")
            mixer.music.play()
            break
alarm()        
