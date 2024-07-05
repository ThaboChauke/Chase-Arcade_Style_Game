import pygame as pg

class BackgroundMusic:

    def __init__(self) -> None:
        pass

    def play_background_music(filepath):
        
        try :
            pg.mixer.init()
            pg.mixer.music.load(filepath)
            pg.mixer.music.play(-1)
        except FileNotFoundError:
            return f"ERROR: {filepath} not found!"
        return True


    def stop_background_music():
        pg.mixer.music.stop()
