from pygame import mixer
import pygame.constants


def music():
    mixer.init()
    mixer.music.load("music/lordapp vol1 preview2.mp3")
    mixer.music.play(-1)
    mixer.music.set_endevent(pygame.constants.USEREVENT)


def introsound():
    mixer.init()
    mixer.music.load("music/introsound.mp3")
    mixer.Channel(1).play(pygame.mixer.Sound('music/introsound.mp3'))
    mixer.music.set_endevent(pygame.constants.USEREVENT)


def mute(volume: float) -> None:
    mixer.music.set_volume(float(volume) / 100)