import os.path
import winsound


def invalidCode():
    winsound.PlaySound(os.path.abspath("Wrong-answer-sound-effect.wav"), winsound.SND_FILENAME)

def drink():
    winsound.PlaySound(os.path.abspath("drink.wav"), winsound.SND_FILENAME)


def horror():
    winsound.PlaySound(os.path.abspath("zoombie.wav"), winsound.SND_FILENAME)

def hazmatSound():
    winsound.PlaySound(os.path.abspath("hazmat.wav"), winsound.SND_FILENAME)

def attack():
    winsound.PlaySound(os.path.abspath("attack.wav"), winsound.SND_FILENAME)
