from pygame import mixer

mixer.init()
mixer.music.load("play.wav")
mixer.music.play()

# import simpleaudio as sa

# wave_obj = sa.WaveObject.from_wave_file("0002075.mp3")
# play_obj = wave_obj.play()
# play_obj.wait_done()
