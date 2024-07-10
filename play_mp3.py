import pygame
import time
import os

#PCにてmp3を再生
def play_mp3(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(0,0.0)
    is_playing = pygame.mixer.music.get_busy()
    while is_playing:
        is_playing = pygame.mixer.music.get_busy()
    pygame.mixer.music.stop()  # 終了
    time.sleep(1)

    pygame.quit()
    os.remove(file_name)

