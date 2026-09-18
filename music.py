import pygame
def music(music_name,volume,model):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.play(model)