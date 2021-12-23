import pygame

pygame.init()
pygame.mixer.music.load('alrme.wav')
pygame.mixer.music.play()

#import simpleaudio as sa

#wave_obj = sa.play_buffer("alarmeDespertador.wav")
#play_obj = wave_obj.play()
#play_obj.wait_done()