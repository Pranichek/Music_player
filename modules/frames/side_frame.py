import pygame
import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_next_song , image_prev_song , image_pause , image_stop, image_play
from .frame_for_songs import list_songs
from threading import Thread , Event

pygame.mixer.init()

list_for_button = []


event_pause = Event()
event_pause.set()

#лист для проверки стоп кнопки
list_check_stop = [0]

def play_song():
    prev_song = " "
    a = 0
    #если песня была поставлена на паузы и мы опять нажали на играть, то чтобы песня начала играть с последнего момента  остоновки
    if not event_pause.is_set():
        #задаем True into event_pause(говорим что сняли песню с паузы)
        event_pause.set()
        pygame.mixer.music.unpause()
    #если музыка не была на паузе то просто отгрываем каждую песню по очереди 
    else:
        while True:
            for song in list_songs:
                a += 1
                # print(a)
                if list_flipping_song[0] == "Back":
                    list_flipping_song[0] = False
                    # print(1)
                    name , file = prev_song.split(".mp3")
                    label_for_show_name.configure(text = name)
                    pygame.mixer.music.load(prev_song)
                    pygame.mixer.music.play()
                    # print(prev_song , "prec_song")
                    # print(song, "song")
                else:
                    # print(2)
                    print(prev_song , "its a prev")
                    if prev_song != " ":
                        index_current_song = list_songs.index(prev_song)
                        song = list_songs[index_current_song + 1]
                    name , file = song.split(".mp3")
                    label_for_show_name.configure(text = name)
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    prev_song = song
                
                for button in list_for_button:
                    if button._text == label_for_show_name._text:
                        button.configure(fg_color = "orange")
                    else:
                        button.configure(fg_color = "#3b8ecf")
                #делаем бесконченый цикл чтобы музыка могла играть , а не сразу остонавливаться
                #если бы его не было , то музыка сразу после включения останавливалась бы либо переклюичалась на другую
                while pygame.mixer.music.get_busy():   
                    pygame.time.Clock().tick(100)
                    #если кнопка следущей песни была нажата, заканчиваем эту иттерацию и перехдим к следущей
                    if list_flipping_song[0] == True:
                        list_flipping_song[0] = False
                        pygame.mixer.music.stop()
                        continue
                    #елси включили песню играть , и в моменте постаивли на паузу, то останавливаем песню и ждем пока пауза будет снята
                    if not event_pause.is_set():
                        pygame.mixer.music.pause()
                        #отсонавливаем поток, и он продолжиться чтолько в том случаем когда в event_pause будет True(event_pause.set()) , то есть снимем с паузы
                        event_pause.wait()
                    
                    #перелистывание назад
                    if list_flipping_song[0] == "Back":
                        for song in list_songs:
                            if song == label_for_show_name._text + ".mp3":
                                index_current_song = list_songs.index(song)
                                prev_song = list_songs[index_current_song - 1]
                                print(prev_song, "Это предыдущая песня")
                                pygame.mixer.music.stop()
                                break
                        
                pygame.mixer.music.stop()
                #если в списке гаходится 1 то значит что был нажата кнопка стоп
                if list_check_stop[0] > 0:
                    #останавливаем песни еще раз на всякий случай
                    pygame.mixer.music.stop()
                    #обнуляем список для отслеживания паузы
                    list_check_stop[0] = 0
                    #выходим из цикла
                    label_for_show_name.configure(text = "Stop")
                    exit()
                if label_for_show_name._text == list_songs[:-1]:
                    if not pygame.mixer.music.get_busy():
                        break

#лист для прелистывания музыки
list_flipping_song = [False]


def next_song():
    list_flipping_song[0] = True
    event_pause.set()
    pygame.mixer.music.unpause()
    # print(label_for_show_name._text + ".mp3")
    if label_for_show_name._text == "Stop":
        list_flipping_song[0] = False
        pass
    else:  
        if list_flipping_song[0] == True and label_for_show_name._text == "Пісня ще не грає":
            # print("заходит")
            play_theread()
            list_flipping_song[0] = False
        elif label_for_show_name._text + ".mp3" == list_songs[-1]:
            # print("в конце списка")
            play_theread()
            list_flipping_song[0] = False


def prev_song():
    list_flipping_song[0] = "Back"
    
        
    
#созадем поток для того тчобы музыка могла играть без бесконечной загрузки
def play_theread():
    play = Thread(target = play_song)
    play.start()


#если event_pause False то это значит пауза
def pause_music():
    #проверяем поставлена ли пауза,находится True значит что пауза не поставлена
    if event_pause.is_set(): 
        #если нажали на паузы то ставим false в event_pause и говорим что сейчас пауза
        event_pause.clear()  
        pygame.mixer.music.pause() 


def stop_music():
     #проверяем поставлена ли пауза,находится True значит что пауза не поставлена, это чтобы если ми нажали сначала на паузу и потом на стоп, то песня все ранво играла с последнего момента
    if event_pause.is_set():
        #остонавливаем песни
        pygame.mixer.music.stop()
        #прибавляем 1 к списку чтобы могли отслеживать поставлена ли пауза
        list_check_stop[0] += 1



#оздание фрейм бара для боковой панели
frame_bar = ctk.CTkFrame(app, width = 169 , height = 298 , fg_color = "#4cb7ce")
frame_bar.place(x = 268 , y = 83)


#настройка колонок и рядков для растановки кнопок на боковой панели
frame_bar.columnconfigure(0 , weight= 1) # | вертикальные колоны
frame_bar.rowconfigure((0 , 1, 2, 3,), weight = 1) # - - - - -  горизонтальные колоны

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

#в строке делаем отступ только с низу с помощью такой стурктуры записи pady = (0 , 10)
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
                                command= next_song
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
                                command= prev_song
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
                            command = stop_music
                            )
#в 57 строке делаем отступ только сверху от кнопки с помощью такой записи pady = (10 , 0)
button_stop.grid(row = 3 , column = 0 , pady = (10 , 0))

#Создаем лейбл для отображения какая музыка сейчас играет
label_for_show_name = ctk.CTkLabel(master = app, text = "Пісня ще не грає" ,width = 160, height = 15 , font = ("Inter" , 16) , text_color = "#FFFFFF")
label_for_show_name.place(x = 270, y = 30)
