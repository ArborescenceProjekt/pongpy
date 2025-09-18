# Créé par ARborescence Projekt, le 17/09/2025 en Python 3.7

import sys, os, pygame, random

pygame.mixer.init()

def ressource_path(relative_path):
        try:
            base_path = sys.MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

class Sound_Manager:

    def __init__(self):
        self.sounds = {
            "sfx_explosion": pygame.mixer.Sound(ressource_path("Sounds/explosion.wav")),
            "sfx_point": pygame.mixer.Sound(ressource_path("Sounds/point.wav")),
            "sfx_ball": [
                pygame.mixer.Sound(ressource_path("Sounds/blipSelect.wav")),
                pygame.mixer.Sound(ressource_path("Sounds/blipSelect2.wav")),
                pygame.mixer.Sound(ressource_path("Sounds/blipSelect3.wav"))
                ],
            "sfx_point_glitched": pygame.mixer.Sound(ressource_path("Sounds/Glitched/point.wav")),
            "sfx_explosion_glitched": pygame.mixer.Sound(ressource_path("Sounds/Glitched/explosion.wav")),
            "sfx_ball_glitched": [
                pygame.mixer.Sound(ressource_path("Sounds/Glitched/blipSelect.wav")),
                pygame.mixer.Sound(ressource_path("Sounds/Glitched/blipSelect2.wav")),
                pygame.mixer.Sound(ressource_path("Sounds/Glitched/blipSelect3.wav"))
                ],
            }
        self.sounds_raw = {
            "sfx_explosion": "Sounds/explosion.wav",
            "sfx_point": "Sounds/point.wav",
            "sfx_ball": [
                "Sounds/blipSelect.wav",
                "Sounds/blipSelect2.wav",
                "Sounds/blipSelect3.wav"
                ]
            }

    def play(self, name):
        sfx = self.sounds.get(name)
        if isinstance(sfx, list):
            random.choice(sfx).play()
        else:
            sfx.play()

    '''def volume_global(self, volume):
        for sound in self.sounds.values():
            if isinstance(sound, list):
                for s in sound:
                    s.set_volume(volume)
            else:
                sound.set_volume(volume)'''



