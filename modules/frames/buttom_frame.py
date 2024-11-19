import pygame
import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_add_song, image_del_song , image_mix_songs , image_sound_up , image_sound_down
import os
from customtkinter import filedialog
import random as r
from .frame_for_songs import frame_treks , list_songs 
from .side_frame import event_pause , list_check_stop , label_for_show_name, list_flipping_song  
from threading import Thread 


pygame.mixer.init()



def open_songs():
    path = filedialog.askdirectory()
    #проверка на то что выбрал ли пользователь директорию (если путь не пустой)
    if path != None:
        name = ""
        #chdir - команда меняет текущую рабочую директорию на указанную в переменной path , чтобы pygame мог проигрывать музыку по названию
        os.chdir(path)
        print(path)
        #listdir - команда возвращает список файлов и папок, находящихся в указанной директории path
        songs = os.listdir(path)
        print(songs)
        # #находим середину фрейма чтобы название песен стояли ровно по середине
        # x = (233 - 173) // 2
        # y = 20
        for song in songs:
            #проверка на то что это файл и он имеет расширение ".mp3" (если это так, то добавляем его в список)  
            if song.endswith(".mp3"):
                #если это так, то разбиваем имя файла на имя и расширение (name , file), split(".mp3") разбивает имя файла на имя и расширение) 
                name , file = song.split(".mp3")
                button = ctk.CTkButton(master= frame_treks , text = name , command=lambda name_of_button = name:change_name_button(name_of_button= name_of_button))

                list_for_button.append(button)
                list_songs.append(song)

            for song in list_for_button:
             song.pack(pady = 10)
                #создаем новый лейбл с названием музыки и добавляем в окно где отображаются название трэков
            #     label = ctk.CTkLabel(frame_treks , text = name ,width = 173) 
            #     #установка позиции лейбла в фрейме , используем place чтобы фрейм не стягивался
            #     label.place(x = x , y = y)
            #     #добавляем музыку в список
            #     list_songs.append(song)
            #     y += 40
            #     # frame_treks._label_text = str(list_songs)
            # # list_songs.remove('.DS_Store')

#лист для хранения кнопок с названиями песен
list_for_button = []

#лист чтобы контрлилоровать удаление песен
check_del = [False]

#функция для каждой кнопки которая добавляется в frame_treks, в параметре name_of_button лежит название кнопки на которую нажали
def change_name_button(name_of_button):
    #если на кнопку удаления нажали то заходим в условие 
    if check_del[0] == True:      
        print(1)   
        #делаем перебор кнопок чтобы понять на какую кнопку нажали
        for button in list_for_button:
            print(2)
            #если текущая кнопка совпадает с кнопкой которую нажали, удаляем ее из окна и из списка для песен
            if button._text == name_of_button:
                # button.configure(text = "Deleting this song")
                #удаляем кнопку из окна
                button.destroy()
                print(name_of_button + ".mp3")
                #удаляем песню из списка песен
                list_songs.remove(name_of_button + ".mp3")
                print(list_songs)
                #передаем в список для контроля кнопки удаления False чтобы чтобы контрлилоровать удаление песен по нажатию на кнопку удаления
                check_del[0] = False
            #если песен уже нет очищаем список кнопко(решение не на долгий срок)
            elif len(list_songs) < 1:
                list_for_button.clear()

#если в check_del лежит False то значит на кнопку удаления не нажали 
def delete_song():
    #передаем True чтобы сказать что нажали на кнопку 
    check_del[0] = True

volume = pygame.mixer.music.get_volume()
list_for_volume = [volume]
pygame.mixer.music.set_volume(list_for_volume[0])

def add_volume():
    list_for_volume[0] += 0.1
    pygame.mixer.music.set_volume(list_for_volume[0])
    print(list_for_volume[0])
    if list_for_volume[0] > 1.1:
        list_for_volume[0] = 1
        pygame.mixer.music.set_volume(list_for_volume[0])

def minus_volume():
    list_for_volume[0] -= 0.1
    pygame.mixer.music.set_volume(list_for_volume[0])
    print(list_for_volume[0])
    if list_for_volume[0] < 0.01:
        list_for_volume[0] = 0
        pygame.mixer.music.set_volume(list_for_volume[0])
    



#лист для проверки чтобы не играла одна и тажа песня два раза
same_song = [""]
#лист для хранения рандомной песни
list_for_random_song = [""]
#list for [rev song
prev_song = [""]
def random_song():
    #если песня была поставлена на паузы и мы опять нажали на играть, то чтобы песня начала играть с последнего момента  остоновки
    if not event_pause.is_set():
        #задаем True into event_pause(говорим что сняли песню с паузы)
        event_pause.set()
        pygame.mixer.music.unpause()
    #если музыка не была на паузе то просто отгрываем каждую песню по очереди 

    for music in range(len(list_songs)):
        if list_flipping_song[0] == "Back":
            list_flipping_song[0] = False
            print(1)
            # if prev_song != " ":
            #     index_current_song = list_songs.index(prev_song)
            #     song = list_songs[index_current_song + 1]
            name , file = prev_song[0].split(".mp3")
            label_for_show_name.configure(text = name)
            pygame.mixer.music.load(prev_song[0])
            pygame.mixer.music.play()
            print(prev_song[0] , "precvsong")
        else:
            #выбираем случайную песню из списка играем ее
            list_for_random_song[0] = r.choice(list_songs)
            name , file  = list_for_random_song[0].split(".mp3")
            #проверяем чтобы эта песня не была одна и таже что и ранее игранная
            while same_song[0] == list_for_random_song[0]:
                    list_for_random_song[0] = r.choice(list_songs)
                    name , file  = list_for_random_song[0].split(".mp3")
                    if same_song[0] != list_for_random_song[0]:
                        print(same_song[0] , "first song")
                        print(list_for_random_song[0] , "second song")
                        break
        
            #меняем текст в лейбле который отображает название текущей песни
            label_for_show_name.configure(text = name)
            pygame.mixer.music.load(list_for_random_song[0])
            pygame.mixer.music.play()

        #делаем бесконечный цикл чтобы музыка могла играть , а не сразу остонавливаться
        while pygame.mixer.music.get_busy():   
                    pygame.time.Clock().tick(100)
                    if list_flipping_song[0] == True:
                        list_flipping_song[0] = False
                        pygame.mixer.music.stop()
                        continue

                    #елси включили песню играть , и в моменте постаивли на паузу, то останавливаем песню и ждем пока пауза будет снята
                    if not event_pause.is_set():
                        pygame.mixer.music.pause()
                        #отсонавливаем поток, и он продолжиться чтолько в том случаем когда в evebt_pause будет True(event_pause.set()) , то есть снимем с паузы
                        event_pause.wait()
                    
                    if list_flipping_song[0] == "Back":
                        pygame.mixer.music.stop()
                        prev_song[0] = same_song[0]
                        break

        
         #если в списке гаходится 1 то значит что был нажата кнопка стоп
        if list_check_stop[0] > 0:
            #останавливаем песни еще раз на всякий случай
            pygame.mixer.music.stop()
            #обнуляем список для отслеживания паузы
            list_check_stop[0] = 0
            label_for_show_name.configure(text = "Stop")
            #выходим из цикла
            break

        same_song[0] = list_for_random_song[0]

        pygame.mixer.music.stop()
        

def random_music_theread():
    random_music = Thread(target = random_song)
    random_music.start()

#фрейм для нижней панели кнопок
frame_buttom = ctk.CTkFrame(master = app , width = 405 , height = 58 , fg_color = "#4cb7ce")
frame_buttom.place(x = 25 , y = 397)

#настройка колонок и рядков для растановки кнопок
frame_buttom.columnconfigure((0,1,2,3,4), weight = 1) #| | | | |
frame_buttom.rowconfigure(0 , weight = 1) # -

buttom_add = ctk.CTkButton(master = frame_buttom , 
                           text= "" ,
                           width = 61 , 
                           height = 58, 
                           fg_color= "#bdbdbd", 
                           border_color = "black" , 
                           corner_radius = 20, 
                           border_width = 4, 
                           image = image_add_song , 
                           anchor = "center" , 
                           command = open_songs)
buttom_add.grid(row = 0 , column = 0 , padx = (0 , 25))

buttom_delete = ctk.CTkButton(master = frame_buttom , 
                              text= "" , 
                              width = 61 , 
                              height = 58, 
                              fg_color= "#bdbdbd", 
                              border_color = "black" , 
                              corner_radius = 20, 
                              border_width = 4, 
                              image = image_del_song , 
                              anchor = "center",
                              command = delete_song)
buttom_delete.grid(row = 0 , column = 1 , padx = (0 , 25))

buttom_mix = ctk.CTkButton(master = frame_buttom , 
                           text= "" , 
                           width = 61 , 
                           height = 58, 
                           fg_color= "#bdbdbd", 
                           border_color = "black" , 
                           corner_radius = 20, 
                           border_width = 4, 
                           image = image_mix_songs , 
                           anchor = "center", 
                           command = random_music_theread
                           ) 
buttom_mix.grid(row = 0 , column = 2, padx = (0 , 25))

button_sound_up = ctk.CTkButton(master = frame_buttom , 
                                text= "" , 
                                width = 61 , 
                                height = 58, 
                                fg_color= "#bdbdbd", 
                                border_color = "black" , 
                                corner_radius = 20, 
                                border_width = 4, 
                                image = image_sound_up , 
                                anchor = "center", 
                                command = add_volume
                                )
button_sound_up.grid(row = 0 , column = 3 , padx = (0 , 25))

button_sound_down = ctk.CTkButton(master = frame_buttom , 
                                  text= "" , 
                                  width = 61 , 
                                  height = 58, 
                                  fg_color= "#bdbdbd", 
                                  border_color = "black" , 
                                  corner_radius = 20, 
                                  border_width = 4, 
                                  image = image_sound_down , 
                                  anchor = "center", 
                                  command = minus_volume
                                  )
button_sound_down.grid(row = 0 , column = 4)








