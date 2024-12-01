# Import module pygame , that can play music
# Імпортуємо модуль pygame , який дозволяє програвати музику
import pygame
# Import module random for randomizing songs
# Імпортуємо модуль який допоможе рандомно програвати музику
import random as r
# Import module os for working with directories
# Імпортуємо модуль який працює із директоріями
import os
# Import module that can create Dekstop programs 
# Імпортуємо необхідний модуль для створення Dekstop програм
import customtkinter as ctk
# Import function that can creates thread 
# Імпортуємо моудль який може створювати потоки 
from threading import Thread 
# Import module that can work with directories of computer
# Імпортуємо модуль який може працювати із директоріями проєкту
from customtkinter import filedialog
# Import main frame , where we places all another frames
# Імпортуємо головний екран , на якому можемо розташовувати всі інші фрейми
from .main_frame import app
# Import images for buttons
# Імпортуємо зображення для кнопок
from ..load_images.get_images import image_add_song, image_del_song , image_mix_songs , image_sound_up , image_sound_down
# Import frame where we places buttons with name of songs
# Імпортуємо фрейм на якому розташовуємо кнопки із назвами пісень
from .frame_for_songs import frame_treks , list_songs 
# Import all lists for manages program
# Імпортуємо всі лісти які допомогають керувати програмою
from .side_frame import event_pause , list_check_stop , label_for_show_name, list_flipping_song  , list_for_button, what_event



pygame.mixer.init()


# A function wich load songs from your computer to music player
# Функціія яка завантажує музику з комп'ютера до музикального плеєра
def open_songs():
    # Choise from wich directory songs will loads to project
    # Запитуємо у користувача із якої дирикторії будемо завантажувати музику
    path = filedialog.askdirectory()
    # Checking that the user does not select an empty directory
    # Перевірка на те , щоб користувач не вибрав пусту директорію
    if path != None:
        name = ""
        # Chdir - the command changes the current working directory to the one specified in the path variable so that pygame can play music by name
        # Chdir - яка команда змінює поточну робочу директорію на вказану в змінній path , щоб pygame міг програвати музику за назвою
        os.chdir(path)
        # os.listdir - a function in Python that returns a list containing the names of the entries in the directory given by path.
        #listdir - команда повертає список файлів та папок, що знаходяться у вказаній директорії path
        songs = os.listdir(path)
        # We go through all the files and check that they have the mp3 extension
        #Перебираємо усі файли , та перевіряємо щоб вони були із розширенням mp3
        for song in songs: 
            if song.endswith(".mp3"):
                # If this is the case, then split the file into name and extension
                # Якщо це так, то розбиваємо файл на ім'я та розширення
                name , file = song.split(".mp3")
                # Create a button with song name ,  - so that the button contains the names of the songs in order, and not just the last one
                # Створення кнопки з назвою пісні , lambda - щоб кнопка містила назви пісень по порядку, а не лише останню
                button = ctk.CTkButton(master= frame_treks , text = name , command=lambda name_of_button = name:change_name_button(name_of_button= name_of_button))

                # Add button to the list of buttons
                # Додаємо кнопку до списку із кнопками
                list_for_button.append(button)

                # Add song to the list for songs
                # Додаємо пісню до списку пісень
                list_songs.append(song)

            # Pack buttons in frame_treks to display them on the screen
            # Розташовуємо кнопки із піснями за допомогою циклу, та робимо відступи у 10 пікселів
            for song in list_for_button:
                song.pack(pady = 10)
                


# List for manage what song need to del
# Ліст для того , щоб контролювати яку пісню треба видаляти
check_del = [False]

# A function that is immediately added for all buttons in the list_sons list; the name_of_button parameter contains the name of the button that was clicked
# Функція, яка відразу додається для всіх кнопок у списку list_sons, у параметрі name_of_button лежить назва кнопки на яку натиснули
def change_name_button(name_of_button):
    # Checking whether you clicked on the delete songs button
    # Перевіряємо чи натиснули на кнопку видалення пісень
    if check_del[0] == True:      
        # We go through the list of buttons with the names of songs to find out which one was clicked
        # Перебираємо всі кнопки з назвами пісень, та перевіряємо чи текуща кнопка совпадает с кнопкой которую нажали, та якщо так, то видаляємо її
        for button in list_for_button:
            # If the song you searched for coincides with the one you clicked on, then delete it
            # Якщо пісня яку перебирали збіглася з тією на яку натиснули, то видаляємо її
            if button._text == name_of_button:
                # If we find the right button, destroy it
                # Якщо нагшли на яку кнопку настиснули , то видаляємо її
                button.destroy()
                # Also delete a song from the list_songs
                # Також видаляємо пісню із списку де зьерігаються усі пісні, щоб її не можна було програти
                list_songs.remove(name_of_button + ".mp3")
                # Also delete the button from the list_for_button
                # Видаляємо кнопку із списка де зберігаються усі кнопки
                list_for_button.remove(button)
                # Transfer the click of the delete button False to the tracking list, so that the next song can be deleted only by clicking on the button
                # Передаємо у список відстеження натискання кнопки видалення False, щоб наступну пісню можна було видалити лише після натискання на кнопку
                check_del[0] = False
            # If already we don't have any buttons in list , clear all list
            # якщо в списку де зберігаються усі кнопки пустий, то очищаємо список
            elif len(list_songs) < 1:
                list_for_button.clear()

# if check_del is False, it means the delete button was not pressed
# якщо в check_del лежить False то значить кнопку видалення не натиснули
def delete_song():
    # transmit True to say that the button was pressed
    # передаємо True щоб сказати що натиснули на кнопку
    check_del[0] = True


# We get what the current volume of the sound is
# Отримуємо яка зараз гучність звуку
volume = pygame.mixer.music.get_volume()
# Save the volume to list
# Зберігаємо гучність у список
list_for_volume = [volume]
# Set volume from the data i list
# Встановлюємо гучність звуку за парметром із списку
pygame.mixer.music.set_volume(list_for_volume[0])

#Fucntion for add volume
# Функція додавання гучності 
def add_volume(): 
    # increase volume by 0.1
    # збільшуємо гучність звуку на 0.1
    list_for_volume[0] += 0.1
    # set the new volume into the mixer music
    # встановлюємо нову гучність звуку 
    pygame.mixer.music.set_volume(list_for_volume[0])
    print(list_for_volume[0])
    # If make volume more the max volume , take it the 1
    # Якщо ми превисили гучність звуку , то встановлюємо 1
    if list_for_volume[0] > 1.1:
        list_for_volume[0] = 1
        pygame.mixer.music.set_volume(list_for_volume[0])


# Function that reduces the volume
# Функція яка зменшує гучність 
def minus_volume():
    # decrease volume by 0.1
    # зменшуємо гучність звуку на 0.1
    list_for_volume[0] -= 0.1
    # set the new volume into the mixer music
    # встановлюємо нову гучність звуку
    pygame.mixer.music.set_volume(list_for_volume[0])
    print(list_for_volume[0])
    # If make volume less the 0, take it the 0
    # Якщо зробили гучність звуку менш ніж 0,01 , то встановлюємо гучність на 0
    if list_for_volume[0] < 0.01:
        list_for_volume[0] = 0
        pygame.mixer.music.set_volume(list_for_volume[0])
    


# Function for playing random song
# Функція для програввання рандомної музики
def random_song():
    # set a list what_event to "random"
    # передаємо у ліст what_event значення "random", це значить що зараз пісні грають на рандом
    what_event[0] = "random"
    # get the initial length of the list of songs
    # отримуємо початкову довжину списку із піснями 
    static_len_list_songs = len(list_songs)
    # a checklist to make sure the same song doesn't play twice
    # список для перевірки щоб не грала одна та тажа пісня два рази
    same_song_list = [None]
    # list of what random song is playing now
    # список яка зараз рандомна пісня грає
    list_for_random_song = [None]
    # leet for storing the previous song
    # лист для зберігання попередньої пісні
    prev_song = [""]
    #if the song was paused and we pressed play again, then the song would start playing from the last moment it was paused
    #якщо пісня була поставлена ​​на паузи і ми знову натиснули на грати, то щоб пісня почала грати з останнього моменту зупинки
    if not event_pause.is_set():
        #we set True into event_pause (we say that we took the song off pause)
        # задаємо True into event_pause (кажемо, що зняли пісню з паузи)
        event_pause.set()
        # unpause the music
        pygame.mixer.music.unpause()
    # If there is no break now, then we just play random songs
    # якщо зараз не пауза, то просто відіграємо рандомні пісні
    else:
        # we make an infinite loop so that the songs play until the stop button is pressed, or until they end
        # робимо нескінченний цикл , для того щоб пісні відігравалися доки не натиснута кнопка стоп, або поки вони не закінчаться
        while True:
            #if there is something stored in the storage list before the last song, then we play the last song before
            #якщо у списку зберігання пред останньої пісні щось зберігається то вілаграємо пред останню пісню
            if prev_song[0] != "":
                # split the song into the name and file extension to output only the song name
                # ділимо пісню на назву та розширення файлу, щоб виводити лише назву пісні
                name , file  = prev_song[0].split(".mp3")
                #Change the label text to show the name of the song currently playing to the name of the previous song
                #Змінюємо текст label для показу назви пісні яка зараз грає , на назву предостаньї пісні
                label_for_show_name.configure(text = name)
                # Play the previous song
                # Відіграємо предостанню пісню
                pygame.mixer.music.load(prev_song[0])
                pygame.mixer.music.play()
                # transfer the current song, previous music to the list
                # Передаємо у список поточної пісні , попередню музику
                list_for_random_song[0] = prev_song[0]
            # If the user hasn't flipped through the songs, we'll just play the next random song.
            # Якщо користувач не перегортав пісні, то просто програємо наступну рандомну пісню
            elif list_for_random_song[0] == same_song_list[-1]:
                if same_song_list[0] == None:
                    same_song_list = []
                
                # Select the next random song from the list
                # Вибираємо наступну рандомну пісню із списку
                list_for_random_song[0] = r.choice(list_songs)
                # doing a search for songs in the list of songs that have already been played
                # Робимо перебор пісень у списку пісень які вже грали
                for same_song in same_song_list:
                    # If such music has already been played, then we randomly select other music that has not been played yet.
                    # Якщо така музика вже грала, то вибираємо рандомно іншу музику якої ще не грала
                    if same_song == list_for_random_song[0]:
                        # do an infinite loop until we find a song that hasn't been played yet
                        # Робимо бескінечний цикл поки не знайдемо пісні яка ще не грала
                        while list_for_random_song[0] in same_song_list:
                            list_for_random_song[0] = r.choice(list_songs)

                # Add the song to the list of songs that have already been played so that it will not be played again next time
                # Додаємо пісню до списку пісень які вже грали , щоб у наступний раз вона вже не грала
                same_song_list.append(list_for_random_song[0])
                # split the song into the name and file extension to output only the song name
                # ділимо пісню на назву та розширення файлу, щоб виводити лише назву пісні
                name , file  = list_for_random_song[0].split(".mp3")
                #Change the label text to show the name of the song that should be playing now.
                #Змінюємо текст label для показу назви пісні яка зараз повинна грати
                label_for_show_name.configure(text = name)
                # Play the selected song
                # Завантажуємо та відіграємо пісню яку вибрали із списку list_songs
                pygame.mixer.music.load(list_for_random_song[0])
                pygame.mixer.music.play()
            
            #If the user scrolled back through the page and now scrolls forward, then execute the code below
            #Якщо користувач перегортав пісін назад , а зараз перегортає у перед , то виконує код нижче
            elif list_for_random_song[0] != same_song_list[-1]:
                #Looking for the song index of the song currently playing
                #Шукаємо індекс пісні яка зараз пісня грає
                index_next_song = same_song_list.index(list_for_random_song[0])
                # By adding to index 1 , select the next song
                # Через додавання до індексу 1 , вибираємо наступну пісню 
                next_song = same_song_list[index_next_song + 1]
                # Update the current song
                # Оновлюємо поточну пісню
                list_for_random_song[0] = next_song
                # split the song into the name and file extension to output only the song name
                # ділимо пісню на назву та розширення файлу, щоб виводити лише назву пісні
                name , file  = next_song.split(".mp3")
                #Change the label text to show the name of the song that should be playing now
                # Змінюємо текст label для показу назви пісні яка зараз повинна грати
                label_for_show_name.configure(text = name)
                # Play the next song
                # Завантажуємо та відіграємо наступну пісню
                pygame.mixer.music.load(next_song)
                pygame.mixer.music.play()
            
            # clear the list for previous song
            # очищаємо список для зберігання попередньої пісні
            prev_song[0] = ""

            # iterate through the list of buttons with song names to understand which one is currently playing
            # Робимо перебор списку кнопок із назвами пісень, щоб зрозуміти яка зараз грає
            for button in list_for_button:
                try:
                    #if the button text matches the lyrics of the song we are currently playing, then we change its color to orange
                    #якщо текст кнопки співпадє з текстом пісні яка зараз граємо, то змінюємо її колір на оранжевий
                    if button._text == label_for_show_name._text:
                        button.configure(fg_color = "orange")
                    #For other buttons, change the color to blue
                    #Для інших кнопок змінюмо колір на синій
                    else:
                        button.configure(fg_color = "#3b8ecf")
                except Exception as error:
                    print(error)
            # make an infinite loop while the music is playing, so that it always plays to the end, and does not immediately skip to the next one
            # Робимо нескінчений цикл поки грає музика, щоб вона зажди грала до кінця , а не одразу перегорталась на наступну
            while pygame.mixer.music.get_busy():  
                # If the user presses the pause button, pause the music and wait until the user presses it again to resume
                # Якщо користувач натиснув кнопку паузи, призупиніть музику та зачекайте, доки користувач не натисне її знову, щоб відновити
                if not event_pause.is_set():
                    pygame.mixer.music.pause()
                    #stop the thread, and it will continue only if evebt_pause is True(event_pause.set()), that is, we will unpause
                    #Зупиняємо потік, і він продовжиться тільки в тому випадку, коли в evebt_pause буде True(event_pause.set()) , тобто знімемо з паузи
                    event_pause.wait()
                # If user presses the "next_song" button , skip the current iteration
                # Якщо користувач натиснув кнопку "наступна пісня", пропускаємо поточний цикл
                if list_flipping_song[0] == True:
                    if len(same_song_list) >= static_len_list_songs:
                        pass
                    else:
                        list_flipping_song[0] = False
                        pygame.mixer.music.stop()
                        continue
                
                # If user presses the "previous_song" button , thne make the codes below
                # Якщо користувач натиснув кнопку "попередня пісня" , робимо код нижче
                if list_flipping_song[0] == "Back":
                    # Stop the music
                    # Зупиняємо музику
                    pygame.mixer.music.stop()
                    #clear the list to store the state of which button is pressed (forward or back)
                    #очищаємо список для зберігання стану яка кнопка нажата(вперед , або назад)
                    list_flipping_song[0] = False
                    # Search an index of current song
                    # Шукаємо індекс пісні яка зараз грає
                    index_song = same_song_list.index(list_for_random_song[0])
                    # If thiis is a first song in the list , just choise again the first song
                    # Якщо це перша пісня в списку, просто знову виберіть першу пісню
                    if index_song < 1:
                        prev_song[0] = same_song_list[index_song]
                    # If it is not the first song in the list , search an index of previous song
                    # Якщо це не перша пісня в списку, знайдіть індекс попередньої пісні
                    else:
                        prev_song[0] = same_song_list[index_song - 1]
                    print(prev_song[0])
               
                # If in the list of check button "stop" more then 1 , it's mean program have to stop the music
                # Якщо в списку перевірочних кнопок «стоп» більше 1, це означає, що програма повинна зупинити музику
                if list_check_stop[0] > 0:
                    # Stop the music
                    # Зупиняємо музику
                    pygame.mixer.music.stop()
                    # Clear the list of check button "stop"
                    # Очищаємо список для перевірки кнопки «стоп»
                    list_check_stop[0] = 0
                    # Change the text of label wich show what song is playing to "Stop" 
                    # Змініть текст мітки, яка показує, яка пісня відтворюється, на "Зупинити"
                    label_for_show_name.configure(text = "Stop")
                    # Exit from loop 
                    # Виходимо із циклу
                    exit()

            # If the list wich save what song alread played more or equal to list of list_songs , exit from the loop
            # Якщо список, який зберігає пісні, які вже грали, більше або дорівнює списку list_songs, вийдіть із циклу
            if len(same_song_list) >= static_len_list_songs:
                print("End of song list")
                break
            pygame.mixer.music.stop()
       
#Function wich create a thread to play random songs
# Функція яка створює та запускає поток для відігравання рандомних пісень
def random_music_theread():
    # Create a thread
    # Створюємо поток 
    random_music = Thread(target = random_song)
    # Start the thread
    # Запускаємо поток
    random_music.start()




# Create a frame for the bottom row of buttons
# Створюємо фрейм  де будемо розставляти кнопки 
frame_buttom = ctk.CTkFrame(master = app , width = 405 , height = 58 , fg_color = "#4cb7ce")
# place this frame at the desired coordinates
# Створюємо фрейм для кнопок які розташовані у нижньому ряду
frame_buttom.place(x = 25 , y = 397)

# Adjust the grid to correctly position objects in this frame
# Робимо налаштування сітки для правильного розтагування об'єктів в цьому фреймі
frame_buttom.columnconfigure((0,1,2,3,4), weight = 1) #| | | | |
frame_buttom.rowconfigure(0 , weight = 1) # -

# Create a button to add songs to project
# Додаемо кнопку яка буде завантажувати пісні до проєкту
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
# Place it in the first(0) row and first(0) column
# Розташоваємо її у першому рядку та першій колонці
buttom_add.grid(row = 0 , column = 0 , padx = (0 , 25))


# Create a button to delete songs from project
# Створюємо кнопку яка буде видаляти пісні
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
# Place it in the first(0) row and second(1) column
# Розташоваємо її у першому рядку та у другій колонці
buttom_delete.grid(row = 0 , column = 1 , padx = (0 , 25))


# Create a button to play random songs
# Створюємо кнпоку яка буде рандомно видігравати пісні
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
# Place it in the first(0) row and third(2) column
# Розташоваємо її у першому рядку та третій колонці
buttom_mix.grid(row = 0 , column = 2, padx = (0 , 25))

# Create button for volume up
# Створюємо кнопку яка буде підвищує гучність
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
# Place it in the first(0) row and fourth(3) column
# Розташоваємо її у першому рядку та четвертій колонці
button_sound_up.grid(row = 0 , column = 3 , padx = (0 , 25))


# Create button for volume down
# Створюємо кнопку яка робить гучність ниже
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
# Place it in the first(0) row and fifth(4) column
# Розташоваємо її у першому рядку та п'ятій колонці
button_sound_down.grid(row = 0 , column = 4)








