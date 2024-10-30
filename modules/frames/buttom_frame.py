import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_add_song, image_del_song , image_mix_songs , image_sound_up , image_sound_down
import os
from customtkinter import filedialog
import random as r
from .frame_for_songs import frame_treks , list_songs 
import pygame
from threading import Thread 
from .side_frame import event_pause , list_check_stop , label_for_show_name


pygame.init()


#фрейм для нижней панели кнопок
frame_buttom = ctk.CTkFrame(master = app , width = 405 , height = 58 , fg_color = "#4cb7ce")
frame_buttom.place(x = 25 , y = 397)

list_with_buttons_song_name = []




class Button(ctk.CTkButton):
    def __init__(self, child_master: object, text:str,command,**kwargs):
        ctk.CTkButton.__init__(
            self, 
            master= child_master, 
            text = text,
            command= command,
            **kwargs
        )
        # self.grid(row= 0, column= 0, sticky= 'nsew')
        self.place(x= 20, y= 20)
        


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
        for song in songs:
            #проверка на то что это файл и он имеет расширение ".mp3" (если это так, то добавляем его в список)  
            if song.endswith(".mp3"):
                #если это так, то разбиваем имя файла на имя и расширение (name , file), split(".mp3") разбивает имя файла на имя и расширение) 
                name , file = song.split(".mp3")
                #создаем новый лейбл с названием музыки и добавляем в окно где отображаются название трэков
                # button= ctk.CTkButton(frame_treks , text = name , command=lambda :change_button(index = len(list_with_buttons_song_name) - 1))
                # button = Button(child_master= frame_treks , text = name , command=lambda index = len(list_with_buttons_song_name):change_button(index = index))
                button = Button(child_master= frame_treks , text = name , command=lambda name_of_button = name:change_button(name_of_button= name_of_button))

                # button_with_song.pack(pady = 10)
                list_with_buttons_song_name.append(button)
                #добавляем музыку в список
                list_songs.append(song)
        #новый сопособ расстановки кнопок с названием песен
        for song in list_with_buttons_song_name:
             song.pack(pady = 10)
             
check_del = [True]
             
def change_button(name_of_button):
    if check_del[0] == False:      
        print(1)   
        for button in list_with_buttons_song_name:
            print(2)
            if button._text == name_of_button:
                button.configure(text = "please")
                button.destroy()
                print(name_of_button + ".mp3")
                list_songs.remove(name_of_button + ".mp3")
                print(list_songs)
                check_del[0] = True
            elif len(list_songs) < 1:
                 list_with_buttons_song_name.clear()

      
# def change_button(index):
#     if check_del[0] == False:
#         print(index , "index")
       
#         del list_songs[index]
#         print(list_songs)
        
#         button = list_with_buttons_song_name[index]
#         button.destroy()

#         del list_with_buttons_song_name[index]

#         # for i, button in enumerate(list_with_buttons_song_name):
#         #     button.id = i
#         #     button.configure(command=lambda i=i: change_button(i))
        
#         for index in range(len(list_with_buttons_song_name)):
#             for button in list_with_buttons_song_name:
#                  button = list_with_buttons_song_name[index]
#                  button.configure(command=lambda index = index: change_button(index))
        
#         check_del[0] = True

        # for button in list_with_buttons_song_name[::-1]:
        #      button.id = len(list_with_buttons_song_name) 
        #      button.configure(command=lambda index = len(list_with_buttons_song_name):change_button(index = index))

        # print(list_songs , "second_time")
             

        # for butto in list_with_buttons_song_name[::-1]:
        #         butto.id -= 1
        #         butto.configure(command=lambda index = len(list_with_buttons_song_name):change_button(index = index))
    #     for bb in list_with_buttons_song_name:
    #          bb.configure(command = lambda: change_button(bb.id))
    #     check_del[0] = True
    # print(index - len(list_with_buttons_song_name) - 1)
    # del list_songs[index - len(list_with_buttons_song_name) - 1]
    # print(list_songs)
#     for i in range(len(list_with_buttons_song_name) - 1):
#         for button in list_with_buttons_song_name:
#             button.id += i
#     for b in list_with_buttons_song_name:
#          print(b.id)
    
    #  del list_songs[index]
    #  print(list_songs)
    #  for button in list_with_buttons_song_name:
    #       if button._text == text_of_button:
    #            print(button._text)
    #            print(list_songs)
        #   if button._hover_color == "green":
        #        button.destroy()

    #  for button in list_with_buttons_song_name:
    #       if button.is_pressed():
              
    #  button_press.configure(text = "r")
    #  for fsf in list_with_buttons_song_name:
    #       if fsf._text == "r":
    #            fsf.destroy()
      
             
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
    



          
          

#если в check_del лежит False то значит на кнопку удаления не нажали 
def delete_song():
    # #проверяем поставлена ли пауза,находится True значит что пауза не поставлена, это чтобы если ми нажали сначала на паузу и потом на стоп, то песня все ранво играла с последнего момента
    # if event_pause.is_set():
    #     #остонавливаем песни
    #     pygame.mixer.music.stop()
    #     #прибавляем 1 к списку чтобы могли отслеживать поставлена ли пауза
    #     list_check_stop[0] += 1
    #     print("Сюда зашло")
        check_del[0] = False




#лист для проверки чтобы не играла одна и тажа песня два раза
same_song = [""]
#лист для хранения рандомной песни
list_for_random_song = [""]
def random_song():
        #если песня была поставлена на паузы и мы опять нажали на играть, то чтобы песня начала играть с последнего момента  остоновки
    if not event_pause.is_set():
        #задаем True into event_pause(говорим что сняли песню с паузы)
        event_pause.set()
        pygame.mixer.music.unpause()
    #если музыка не была на паузе то просто отгрываем каждую песню по очереди 
    
    for music in range(len(list_songs)):
    
        #выбираем случайную песню из списка играем ее
        list_for_random_song[0] = r.choice(list_songs)
        name , file  = list_for_random_song[0].split(".mp3")


        #проверяем чтобы эта песня не была одна и таже что и ранее игранная
        while same_song[0] == list_for_random_song[0]:
                list_for_random_song[0] = r.choice(list_songs)
                name , file  = list_for_random_song[0].split(".mp3")
                if same_song[0] != list_for_random_song[0]:
                    break
    
        #меняем текст в лейбле который отображает название текущей песни
        label_for_show_name.configure(text = name)
        pygame.mixer.music.load(list_for_random_song[0])
        pygame.mixer.music.play()

        #делаем бесконечный цикл чтобы музыка могла играть , а не сразу остонавливаться
        while pygame.mixer.music.get_busy():   
                    pygame.time.Clock().tick(100)

                    #елси включили песню играть , и в моменте постаивли на паузу, то останавливаем песню и ждем пока пауза будет снята
                    if not event_pause.is_set():
                        pygame.mixer.music.pause()
                        #отсонавливаем поток, и он продолжиться чтолько в том случаем когда в evebt_pause будет True(event_pause.set()) , то есть снимем с паузы
                        event_pause.wait()
        
         #если в списке гаходится 1 то значит что был нажата кнопка стоп
        if list_check_stop[0] > 0:
            #останавливаем песни еще раз на всякий случай
            pygame.mixer.music.stop()
            #обнуляем список для отслеживания паузы
            list_check_stop[0] = 0
            #выходим из цикла
            break

        same_song[0] = list_for_random_song[0]

        pygame.mixer.music.stop()
        

def random_music_theread():
    random_music = Thread(target = random_song)
    random_music.start()


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
                              command= delete_song
                            )
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








