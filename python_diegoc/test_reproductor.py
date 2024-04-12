from tkinter import * 
#from t import *
from reproductor import *

musica = Reproductor("wefere.mp3")
display = "Iniciando"

def play_musica():
    musica.volume(0.8)
    musica.play()
    label.config(text = display)

def pause_musica():
    musica.pause()
    label.config(text = display)

def stop_musica():
    musica.stop



master = Tk()
master.geometry("200x200")
label = Label(master, text = display)

label = Label(master, text = "Reproductor de música")

label.pack(pady = 10)

btn_play = Button(master,text = "Reproducir", command = play_musica)
btn_play.pack(pady = 10)

btn_play = Button(master,text = "Pausar", command = pause_musica)
btn_play.pack(pady = 10)

btn_play = Button(master,text = "Detener", command = stop_musica)
btn_play.pack(pady = 10)

mainloop()