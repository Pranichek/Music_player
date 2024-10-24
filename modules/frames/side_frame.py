import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_next_song , image_prev_song , image_pause , image_stop, image_play
import pygame
from .frame_for_songs import list_songs
from threading import Thread 
import threading

pygame.init()

list_for_count_song = [0]

#оздание фрейм бара для боковой панели
frame_bar = ctk.CTkFrame(app, width = 169 , height = 298 , fg_color = "#4cb7ce")
frame_bar.place(x = 268 , y = 83)


#настройка колонок и рядков для растановки кнопок на боковой панели
frame_bar.columnconfigure(0 , weight= 1) # | вертикальные колоны
frame_bar.rowconfigure((0 , 1, 2, 3,), weight = 1) # - - - - -  горизонтальные колоны

print(list_songs)

event_pause = threading.Event()
event_pause.set()

def play_song():
    #если песня была поставлена на паузы и мы опять нажали на играть, то чтобы песня начала играть с последнего момента  остоновки
    if not event_pause.is_set():
        #задаем True into event_pause(говорим что сняли песню с паузы)
        event_pause.set()
        pygame.mixer.music.unpause()
    #если музыка не была на паузе то просто отгрываем каждую песню по очереди 
    else:
        for song in list_songs:
            name , file = song.split(".mp3")
            label_for_show_name.configure(text = name)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            #делаем бесконченый цикл чтобы музыка могла играть , а не сразу остонавливаться
            #если бы его не было , то музыка сразу после включения останавливалась бы либо переклюичалась на другую
            while pygame.mixer.music.get_busy():   
                pygame.time.Clock().tick(100)

                #елси включили песню играть , и в моменте постаивли на паузу, то останавливаем песню и ждем пока пауза будет снята
                if not event_pause.is_set():
                    pygame.mixer.music.pause()
                    #отсонавливаем поток, и он продолжиться чтолько в том случаем когда в evebt_pause будет True(event_pause.set()) , то есть снимем с паузы
                    event_pause.wait()

            pygame.mixer.music.stop()

#созадем поток для того тчобы музыка могла играть без бесконечной загрузки
def play_theread():
    play = Thread(target = play_song)
    play.start()
    
    
#если event_pause False то это значит пауза
def pause_music():
    #проверяем поставлена ли пауза,находится True значит что пауза не поставлен
    if event_pause.is_set(): 
        #если нажали на паузы то ставим false в event_pause и говорим что сейчас пауза
        event_pause.clear()  
        pygame.mixer.music.pause() 

    
       
        

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
                             command = play_theread)

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
                            command = pause_music,
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

#Создаем лейбл для отображения какая музыка сейчас играет
label_for_show_name = ctk.CTkLabel(master = app, text = "Пісня ще не грає" ,width = 160, height = 15 , font = ("Inter" , 16) , text_color = "#FFFFFF")
label_for_show_name.place(x = 270, y = 30)
