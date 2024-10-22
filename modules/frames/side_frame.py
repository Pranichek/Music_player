import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_next_song , image_prev_song , image_pause , image_stop, image_play
from pygame import mixer
import pygame
from .frame_for_songs import list_songs
import time as t 

pygame.init()

list_for_count_song = [0]

#оздание фрейм бара для боковой панели
frame_bar = ctk.CTkFrame(app, width = 169 , height = 298 , fg_color = "#4cb7ce")
frame_bar.place(x = 268 , y = 83)


#настройка колонок и рядков для растановки кнопок на боковой панели
frame_bar.columnconfigure(0 , weight= 1) # | вертикальные колоны
frame_bar.rowconfigure((0 , 1, 2, 3,), weight = 1) # - - - - -  горизонтальные колоны

print(list_songs)
list_music = []
start = []

def play_song():
    start.append(1) 
    # for trak in list_songs:
    #     list_music.append(pygame.mixer.Sound(trak))
      
    k = pygame.mixer.Channel(1)

    for song in list_songs:
        mixer.music.load(song)
        mixer.music.play()
        while pygame.mixer.music.get_busy():   
            pygame.time.Clock().tick(100)
        
        pygame.mixer.music.stop()

#создание кнопок для фрейма frame_bar
button_play = ctk.CTkButton(master= frame_bar ,
                             text = "",
                             width = 169 , 
                             height = 60 , 
                             fg_color= "#bdbdbd" , 
                             border_color = "black", 
                             corner_radius= 20 , 
                             border_width= 4 , 
                             image= image_play , 
                             anchor = "center",
                             command=play_song)

#в  строке делаем отступ только с низу с помощью такой стурктуры записи pady = (0 , 10)
button_play.grid(row = 0 , column = 0 , pady = (0 , 10))

button_next_song = ctk.CTkButton(master= frame_bar ,
                                text= "" ,
                                width = 61 , 
                                height = 58, 
                                fg_color= "#bdbdbd", 
                                border_color = "black" ,
                                corner_radius = 20, 
                                border_width = 4 , 
                                image=image_next_song , 
                                anchor = "center",
                                )
button_next_song.grid(row = 1 , column = 0 , sticky = "w", pady = 10)

button_prev_song = ctk.CTkButton(master = frame_bar, 
                                text= "" ,
                                width = 61 , 
                                height = 58, 
                                fg_color= "#bdbdbd", 
                                border_color = "black" , 
                                corner_radius = 20, 
                                border_width = 4, 
                                image= image_prev_song, 
                                anchor="center",
                                )
button_prev_song.grid(row = 1 , column = 0 , sticky = "e", pady = 10)

button_pause = ctk.CTkButton(master = frame_bar , 
                            text = "", 
                            width = 169, 
                            height = 60 , 
                            fg_color= "#bdbdbd", 
                            border_color = "black" , 
                            corner_radius = 20, 
                            border_width = 4, 
                            image = image_pause , 
                            anchor = "center", 
                            )
button_pause.grid(row = 2 , column = 0 , pady = 10)

button_stop = ctk.CTkButton(master = frame_bar , 
                            text = "", 
                            width = 169 , 
                            height = 60 , 
                            fg_color= "#bdbdbd", 
                            border_color = "black" , 
                            corner_radius = 20, 
                            border_width = 4, 
                            image = image_stop , 
                            anchor= "center", 
                            )
#в 57 строке делаем отступ только сверху от кнопки с помощью такой записи pady = (10 , 0)
button_stop.grid(row = 3 , column = 0 , pady = (10 , 0))

