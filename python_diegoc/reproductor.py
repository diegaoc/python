from pygame import mixer
class Reproductor:
    #atributos
    archivo = None
    
    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    
    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"
    
    def stop(self):
        mixer.music.stop()
        return "La música se detuvo"
    
    def volume(self, v):
        self.valor_volumen += v
        if(self.valor_volumen >= 1):
            self.valor_volumen = 1
        elif(self.valor_volumen <= 0):
            self.valor_volumen = 0

        mixer.music.set_volume(self.valor_volumen)
        return "Volumen a ", self.valor_volumen
    