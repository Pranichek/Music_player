import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_next_song , image_prev_song , image_pause , image_stop, image_play
from pygame import mixer
from .frame_for_songs import list_songs

mixer.init()

#оздание фрейм бара для боковой панели
frame_bar = ctk.CTkFrame(app, width = 169 , height = 298 , fg_color = "#4cb7ce")
frame_bar.place(x = 268 , y = 83)

number_song = 0
check_music = True

#настройка колонок и рядков для растановки кнопок на боковой панели
frame_bar.columnconfigure(0 , weight= 1) # | вертикальные колоны
frame_bar.rowconfigure((0 , 1, 2, 3,), weight = 1) # - - - - -  горизонтальные колоны

def next_song():
    try:
        global number_song, check_music 
        mixer.music.stop()
        print(number_song , "hahah")
        #добалвяем к переменной которая отслеживает какая музыка играет единичку чтобы начала играть следущая песня
        number_song += 1
        #если эта переменная стала боьлше чем длина списка где хранятся название песен , то переменная обнулялась и начинала играть заново
        if number_song > len(list_songs) - 1:
            number_song = 0
        
        #берем название песни которая сейчас должна играть
        song_name = list_songs[number_song]
        #загружаем музыку которую нужно играть , и включаем ее
        mixer.music.load(song_name)
        mixer.music.play()
        #тут мы записываем на False нашу переменную чтобы когда пользователь нажал на плей музыка начала играть с того момента где был стоп
        check_music = False
        name , file = song_name.split(".mp3")
        label_track_name.configure(text = str(name))
    except IndexError:
        print("You don't have any nusic yet")

def prev_music():
    try:
        global number_song, check_music 
        mixer.music.stop()
        
        #отнимаем от переменной которая отслеживает какая музыка играет единичку чтобы начала играть следущая песня
        number_song -= 1
        #если эта переменная стала меньше нуля , то в переменную записывается номер последней песни чтобы начинала играть последняя песня(переход с первой на последнюю песню)
        if number_song < 0:
            number_song = len(list_songs) - 1
        print(number_song , "hahah")

        #берем название песни которая сейчас должна играть  и включаем ее
        song_name = list_songs[number_song]
        mixer.music.load(song_name)
        mixer.music.play()
        #тут мы записываем на False нашу переменную чтобы когда пользователь нажал на плей музыка начала играть с того момента где был стоп
        check_music = False
        name , file = song_name.split(".mp3")
        label_track_name.configure(text = str(name))
    except IndexError:
        print("You don't have any nusic yet")


  
def stop_song():
    global number_song,check_music 
    #остонавливаем песню 
    mixer.music.stop()
    #обнуляем переменную которая отслеживает какая музыка играет , чтобы при нажатии на кнопку играть начинала играть первая музыка в списке
    number_song = 0
    #записываем в check_music True чтобы  при нажатии на кнопку играть , музыка начинала играть не с того места где остановилась ,а с самого начала (и самая первая в писке будет играть песня)
    check_music = True

def pause_song():
    global check_music,number_song
    #проверка если пользователь нажал сканала на кнопку stop и потом "случайно" на кнопку паузы то когда человек нажмет на старт то музыка начинала все равно играть
    if check_music == True:
        pass
    else:
        mixer.music.pause()
        #записываем в переменную False чтобы когда человек потом нажал на плей(играть), то музыка играла с того момента где остановилась
        check_music = False
        print(check_music)
    

#создание label для название трэка который играет
label_track_name = ctk.CTkLabel(master = app, text = "Ще немає ввімкненої пісні", font = ("Inter", 16),  width = 160 , height = 59, text_color = "white")
label_track_name.place(x = 270, y = 15)

def play_song():
    global number_song , check_music 
    #тут идет проверка стоит ли музыка на паузе если chek_music равно False то мы не заново включаем музыку(с самого начала) а просто снимаем с паузы чтобы она начинала играть где и останановаилась в последний момент.
    #Если check_music = True то это значит что музыку не ставили , а поставили на стоп и музыка будет начинаться с самого начала
    if check_music == True:
        for music in list_songs:
            print(music)
            name , file = music.split(".mp3")
            label_track_name.configure(text = str(name))
            #загружаем и включаем первую песню
            mixer.music.load(music)
            mixer.music.play()
            #тут в переменную записываем False чтобы если мы нажали на кнопку стоп(в этой переменной тогда хранится True) ,а потом на старт , то чтобы потом смогли потом опять поставить на паузу
            #если бы мы этого не делали то просто напросто не смогли бы нажимать на паузу
            check_music = False
            break
    #если chek_music равно False то мы не заново включаем музыку(с самого начала) а просто снимаем с паузы чтобы она начинала играть где и останановаилась в последний момент.
    elif check_music == False:
        mixer.music.unpause()

    #если chek_music равно False то мы не заново включаем музыку(с самого начала) а просто снимаем с паузы чтобы она начинала играть где и останановаилась в последний момент.
    elif check_music == False:
        mixer.music.unpause()
        
    


#создание кнопок для фрейма frame_bar
button_play = ctk.CTkButton(master= frame_bar , text = "",width = 169 , height = 60 , fg_color= "#bdbdbd" , border_color = "black", corner_radius= 20 , border_width= 4 , image= image_play , anchor = "center",command=play_song)
#в 44 строке делаем отступ только с низу с помощью такой стурктуры записи pady = (0 , 10)
button_play.grid(row = 0 , column = 0 , pady = (0 , 10))

button_next_song = ctk.CTkButton(master= frame_bar ,text= "" ,width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4 , image=image_next_song , anchor = "center",command = next_song)
button_next_song.grid(row = 1 , column = 0 , sticky = "w", pady = 10)

button_prev_song = ctk.CTkButton(master = frame_bar, text= "" ,width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image= image_prev_song, anchor="center",command = prev_music)
button_prev_song.grid(row = 1 , column = 0 , sticky = "e", pady = 10)

button_pause = ctk.CTkButton(master = frame_bar , text = "", width = 169, height = 60 , fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_pause , anchor = "center", command = pause_song)
button_pause.grid(row = 2 , column = 0 , pady = 10)

button_stop = ctk.CTkButton(master = frame_bar , text = "", width = 169 , height = 60 , fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_stop , anchor= "center", command = stop_song)
#в 57 строке делаем отступ только сверху от кнопки с помощью такой записи pady = (10 , 0)
button_stop.grid(row = 3 , column = 0 , pady = (10 , 0))

