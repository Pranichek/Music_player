import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_add_song, image_del_song , image_mix_songs , image_sound_up , image_sound_down
from pygame import mixer
import os
from customtkinter import filedialog
from .frame_for_songs import frame_treks , list_songs

mixer.init()



#фрейм для нижней панели кнопок
frame_buttom = ctk.CTkFrame(master = app , width = 405 , height = 58 , fg_color = "#4cb7ce")
frame_buttom.place(x = 25 , y = 397)


def open_songs():
    path = filedialog.askdirectory()
    #проверка на то что выбрал ли пользователь директорию (если путь не пустой)
    if path:
        name = ""
        #chdir - команда меняет текущую рабочую директорию на указанную в переменной path , чтобы pygame мог проигрывать музыку по названию, короче меняем путь нашего файла на путь к папке где музыка
        os.chdir(path)
        print(path)
        #listdir - команда возвращает список файлов и папок, находящихся в указанной директории path
        songs = os.listdir(path)
        print(songs)
        for song in songs:
            #проверка на то что это файл и он имеет расширение ".mp3" (если это так, то добавляем его в список)  
            if song.endswith(".mp3"):
                #если это так, то разбиваем имя файла на имя и расширение (name , file), split(".mp3") разбивает имя файла на имя и расширение) 
                name , file = song.split(".mp3")
                #создаем новый лейбл с названием музыки и добавляем в окно где отображаются название трэков
                label = ctk.CTkLabel(frame_treks , text = name)
                label.pack(pady = 10)
                #добавляем музыку в список
                list_songs.append(song)
                # frame_treks._label_text = str(list_songs)

volume = mixer.music.get_volume()
mixer.music.set_volume(1)
def add_volume():
    global volume
    volume += 0.1
    mixer.music.set_volume(volume)
    print(volume)
    if volume > 1.1:
        volume = 1
        mixer.music.set_volume(volume)
def minus_volume():
    global volume
    volume -= 0.1
    mixer.music.set_volume(volume)
    print(volume)
    if volume < 0.01:
        volume = 0
        mixer.music.set_volume(volume)
    

#настройка колонок и рядков для растановки кнопок
frame_buttom.columnconfigure((0,1,2,3,4), weight = 1) #| | | | |
frame_buttom.rowconfigure(0 , weight = 1) # -

buttom_add = ctk.CTkButton(master = frame_buttom , text= "" ,width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_add_song , anchor = "center" , command = open_songs)
buttom_add.grid(row = 0 , column = 0 , padx = (0 , 25))

buttom_delete = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_del_song , anchor = "center")
buttom_delete.grid(row = 0 , column = 1 , padx = (0 , 25))

buttom_mix = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_mix_songs , anchor = "center")
buttom_mix.grid(row = 0 , column = 2, padx = (0 , 25))

button_sound_up = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_sound_up , anchor = "center", command = add_volume)
button_sound_up.grid(row = 0 , column = 3 , padx = (0 , 25))

button_sound_down = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_sound_down , anchor = "center", command = minus_volume)
button_sound_down.grid(row = 0 , column = 4)







