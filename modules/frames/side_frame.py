# Import module pygame , that can play music
# Імпортуємо модуль pygame , який дозволяє програвати музику
import pygame
# Import module that can create Dekstop programs 
# Імпортуємо необхідний модуль для створення Dekstop програм
import customtkinter as ctk
# Import main frame , where we places all another frames
# Імпортуємо головний екран , на якому можемо розташовувати всі інші фрейми
from .main_frame import app
# Import images for buttons
# Імпортуємо зображення для кнопок
from ..load_images.get_images import image_next_song , image_prev_song , image_pause , image_stop, image_play
# Import list of songs
# Імпортуємо список у якому зьерігаються усі пісні
from .frame_for_songs import list_songs
# Import function that can creates thread 
# Імпортуємо моудль який може створювати потоки 
from threading import Thread , Event

pygame.mixer.init()

# Create a list for save buttons with names of songs
# Створюжмо список для зберігання кнопок із назвами пісень
list_for_button = []
# A list that allows us to move forward or backward through a song
# Список завдяки якому розуміємо вперед або назад треба пролестнути пісню
list_flipping_song = [False]
# Create a list for check "stops" button
# Створюмо список для перевірки натискання кнопки "stop"
list_check_stop = [0]
# Create a list in order to understand whether the songs are currently playing in turn or randomly.
# Створюжмо список для того щоб розуміти зараз пісні по черзі грають чи на рандом
what_event = [None]
# A list for storing the last (or currently playing songs) song, so that you can flip back and find the previous song
# Лист для зберігання останньої (або яка зараз грає пісні), щоб можна було перегорнути назад і знайти попередню пісню 
index_current_song = [0]
# list so that when the music was playing and the last song was played, it was possible to switch back
# список щоб коли грала музика і закінчилася остання, можна було перегорнути назад
previous_track = [""]

# Creat an object to track the music thread ,and set him to the True
# Створюємо об'єкт для відстеження потоку програвання музики , та задаємо йому значення True
event_pause = Event()
event_pause.set()


# Creat a function to play music in turn
# Створюємо функцію для програвання музики по черзі
def play_song():
    # Pass it to the "queue" list to know that the songs are currently playing in turn
    # Передаємо у список "queue" щоб знати що зараз пісні по черзі грають
    what_event[0] = "queue"
    # A copy of the song list so I can find the next song if I delete the one that is currently playing
    # Копія списку пісень щоб можна було знайти наступну пісню якщо вилучила ту, яка зараз грає
    copy_list_songs = list_songs.copy()
    # Variable to store the previous song
    # Змінна для зберігання попередньої пісні
    prev_song = " "
    # If the song was paused and we pressed play again, then the song would start playing from the last moment it was paused
    # Якщо пісня була поставлена ​​на паузи і ми знову натиснули на грати, то щоб пісня почала грати з останнього моменту зупинки
    if not event_pause.is_set():
        # set True into event_pause (say that the song was unpaused)
        # задаємо True в event_pause (кажемо що зняли пісню з паузи)
        event_pause.set()
        pygame.mixer.music.unpause()
    #if the music wasn't paused then we just play each song in turn
    #якщо музика не була на паузі, то просто відграємо кожну пісню по черзі
    else:
        # CREATE THE INFINIY CYCLE
        # СТВОРЮЄМО НЕСКІНЧЕННИЙ ЦИКЛ
        while True:
            # going through the list of songs so that we can play them in turn
            # Перебираємо список пісень щоб можна було відігравати їх по черзі
            for song in list_songs:
                #Condition so that when music is playing and the last one ends, it is possible to rewind the song
                #Умова для того, щоб коли грала музика і закінчилася остання, можна було назад перегорнути пісню назад
                if previous_track[0] ==  "needback" and list_flipping_song[0] == "Back":
                    # Checking if this is actually the last song
                    # Перевіряємо чи є це насправді остання пісня
                    if song == list_songs[-1]:
                        # reset the value of the list, thanks to which we understand whether we need to skip the song forward or backward.
                        # Обнуляємо значення списку завдяки якому розуміємо вперед або назад треба пролестнути пісню
                        list_flipping_song[0] = False
                        # Determine the index of the song that played last
                        # Визначаємо індекс пісні яка грала останньою
                        index_current_song[0] = list_songs.index(song)
                        # Thanks to the index we found, we select the penultimate song from the list.
                        # Завдяки індексу який знайшли , вибираємо із списку пред останню пісню
                        prev_song = list_songs[index_current_song[0] - 1]
                        # split the song into the name and file extension to output only the song name
                        # ділимо пісню на назву та розширення файлу, щоб виводити лише назву пісні
                        name , file = prev_song.split(".mp3")
                        # Change the label text to show the name of the song currently playing to the name of the previous song
                        # Змінюємо текст label для показу назви пісні яка зараз грає , на назву предостаньї пісні
                        label_for_show_name.configure(text = name)
                        # Play the previous song
                        # Відіграємо предостанню пісню
                        pygame.mixer.music.load(prev_song)
                        pygame.mixer.music.play()
                        # reset the value of the variable that stores the previous song
                        # Обнуляємо значення змінної , яка  зберігає попередню пісню
                        previous_track[0] = ""
                    # If this is not the last song, then we simply skip this iteration of the loop.
                    # Якщо це не є останньою піснею ,то просто скіпаємо цю іттерацію циклу
                    else:
                        continue 
                
                # If the list value says to rewind the song, then we perform the throw below
                # Якщо значення списку говорить що треба перегорнути пісню назад , то виконуємо кид нижче
                elif list_flipping_song[0] == "Back":
                    # reset the value of the list, thanks to which we understand whether we need to skip the song forward or backward.
                    # Обнуляємо значення списку завдяки якому розуміємо вперед або назад треба пролестнути пісню 
                    list_flipping_song[0] = False
                    # split the song into the name and file extension to output only the song name
                    # ділимо пісню на назву та розширення файлу, щоб виводити лише назву пісні
                    name , file = prev_song.split(".mp3")
                    # Change the label text to show the name of the song currently playing to the name of the previous song
                    # Змінюємо текст label для показу назви пісні яка зараз грає , на назву попередної пісні
                    label_for_show_name.configure(text = name)
                    # Play the previous song
                    # Відіграємо попередню пісню
                    pygame.mixer.music.load(prev_song)
                    pygame.mixer.music.play()
                # If none of the above conditions worked, then we just play the song one by one.
                # Якщо ніяка із вище написаних умов не спрацювала , то просто відіграємо пісню по черзі
                else:
                    # If we were scrolling back through the songs, we would do the code below
                    # Якщо ми перегортали пісні назад , робимо код нижче
                    if prev_song != " ":
                        try:
                            # trying to find the index of the previous song to find the next one to play.
                            # Намагаємось знайти індекс попереднньої пісні , щоб знайти наступну яку повинні відігравати
                            index_current_song[0] = list_songs.index(prev_song)
                        except Exception as error:
                            # If this song was deleted, then we take the index from the copied list
                            # Якщо цю пісню видалили , то беремо індекс із скопійованного списку
                            if error == ValueError:
                                index_current_song[0] = copy_list_songs.index(prev_song)
                                continue
                        # Checking that this is not the last song in the list
                        # Перевіряємо щоб це не була остання пісня у списку
                        if index_current_song[0] + 1 < len(list_songs):
                            # Thanks to finding the index of the previous song, we are looking for the song that should be played now.
                            # Завдяки тому що знайшли індекс попередньої пісні, шукаємо ту пісню яку повинні зараз відігравати
                            song = list_songs[index_current_song[0] + 1]
                        # If this is the last song, we just exit the loop.
                        # Якщо це остання пісня, то просто виходимо із циклу
                        else:
                            print("This is the last song in the list")
                            exit()
                    # split the song into the name and file extension to output only the song name
                    # ділимо пісню на назву та розширення файлу, щоб виводити лише назву пісні
                    name , file = song.split(".mp3")
                    # Change the label text to display the name of the song currently playing to the name of the current song
                    # Змінюємо текст label для показу назви пісні яка зараз грає , на назву поточної пісні
                    label_for_show_name.configure(text = name)
                    # Load and play the current song
                    # Завантажуємо та відіграємо поточну пісню
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    # set the name of the current song to a variable to store the previous song, so that later it is easy to find the previous one
                    # Задаємо назву поточної пісні , для змінної збереження попередньої пісні, щоб потім легко знайти попередню
                    prev_song = song
                # iterate through the list of buttons with song names to understand which one is currently playing
                # Робимо перебор списку кнопок із назвами пісень, щоб зрозуміти яка зараз грає
                for button in list_for_button:
                    #if the button text matches the lyrics of the song we are currently playing, then we change its color to orange
                    #якщо текст кнопки співпадє з текстом пісні яка зараз граємо, то змінюємо її колір на оранжевий
                    try:
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
                    pygame.time.Clock().tick(100)
                    # If user presses the "next_song" button , skip the current iteration
                    # Якщо користувач натиснув кнопку "наступна пісня", пропускаємо поточний цикл
                    if list_flipping_song[0] == True:
                        list_flipping_song[0] = False
                        pygame.mixer.music.stop()
                        continue
                    # If the user presses the pause button, pause the music and wait until the user presses it again to resume
                # Якщо користувач натиснув кнопку паузи, призупиніть музику та зачекайте, доки користувач не натисне її знову, щоб відновити
                    if not event_pause.is_set():
                        # Pause the music
                        # Ставимо на паузу пісні
                        pygame.mixer.music.pause()
                        # stop the thread, and it will continue only if evebt_pause is True(event_pause.set()), that is, we will unpause
                        # Зупиняємо потік, і він продовжиться тільки в тому випадку, коли в evebt_pause буде True(event_pause.set()) , тобто знімемо з паузи
                        event_pause.wait()
                    
                     # If user presses the "previous_song" button , thne make the codes below
                    # Якщо користувач натиснув кнопку "попередня пісня" , робимо код нижче
                    if list_flipping_song[0] == "Back":
                        # doing a song crawl to find what song is currently playing
                        # Робимо перебор пісень щоб знайти яка піснія зараз грає
                        for song in list_songs:
                            # If we found it, then we do the code below
                            # Якщо ми її знайшли, то робимо код нижче
                            if song == label_for_show_name._text + ".mp3":
                                # Find the index of the current song to find the penultimate song
                                # Знаходимо індекс поточної пісні, щоб знайти предостанню пісню
                                index_current_song[0] = list_songs.index(song)
                                # Find the penultimate song by index
                                # За індексом знаходимо предостанню пісню
                                prev_song = list_songs[index_current_song[0] - 1]
                                # Stop the music
                                # Зупиняємо музику
                                pygame.mixer.music.stop()
                                # skip the current iteration
                                # пропускаємо поточний цикл
                                break
                        
                pygame.mixer.music.stop()
                
                # if there is 1 in the list, it means that the stop button was pressed
                # якщо в списку йде 1, то означає, що була нажата кнопка стоп
                if list_check_stop[0] > 0:
                    # Stop the music
                    # Зупинняємо музику
                    pygame.mixer.music.stop()
                    # Clear the list for check "stops" button
                    # Очистити список для перевірки кнопки «зупинки».
                    list_check_stop[0] = 0
                    # Change label of text for show name of current song to "Stop"
                    # Заміняємо label для показу назви поточної пісні, на текст "Stop"
                    label_for_show_name.configure(text = "Stop")
                    # Exit from loop
                    # Виходимо із циклу
                    exit()
                


# Function for fast-forwarding a song
# Функція для перегортанння пісні уперед
def next_song():
    # Pass the value True to the list to check where the song should be flipped
    # Передаємо у список для перевірки куди треба перегорнути пісню значення True
    list_flipping_song[0] = True
    # Unpause the song if it was paused
    # Знімаємо пісню з паузи, якщо вона стояла
    event_pause.set()
    pygame.mixer.music.unpause()
    # If the songs are currently playing in turn, then we do the code below
    # Якщо зараз пісні грають по черзі , то робимо код нижче 
    if what_event[0] == "queue" or what_event[0] != "random":
        # If it is currently at stop, then we do nothing
        # Якщо зараз стоїть стоп , то нічого не робимо
        if label_for_show_name._text == "Stop":
            # We reset the value in the list to zero to check where to scroll the songs - forward or backward
            # Обнуляємо значення у списку для перевірки куди треба перегорнути пісні - вперед чи назад
            list_flipping_song[0] = False
            pass
        # If there is no stop now, then we do the code below
        # Якщо зараз немає стопу , то робимо код нижче
        else: 
            # If the user has never played music before (i.e. this is the first time they have started the program), then it starts playing songs one after the other
            # Якщо користувач ніколи ще не запускав музику(тобто вперший раз запустив програму) , то запускає прогрвання пісень одна за одною
            if list_flipping_song[0] == True and label_for_show_name._text == "Пісня ще не грає":
                play_theread()
                # Reset the value in the list to zero to check where to scroll the songs - forward or backward
                # Обнуляємо значення у списку для перевірки куди треба перегорнути пісні - вперед чи назад
                list_flipping_song[0] = False
            # If user flipped the song to the first (i.e. it was the last one, and flipped to the first one)
            # Якщо користувач перегорнули пісню на першу(тобто була остання , та перегорнули на першу) 
            elif label_for_show_name._text + ".mp3" == list_songs[-1]:
                # Then we start the stream of playing songs one after another
                # Тоді запускаємо поток прогрвання пісень одна за одною
                play_theread()
                # Reset the value in the list to zero to check where to scroll the songs - forward or backward
                # Обнуляємо значення у списку для перевірки куди треба перегорнути пісні - вперед чи назад
                list_flipping_song[0] = False

# Function to rewind songs
# Функція для перегортання пісень назад
def prev_song():
    # Pass the value "Back" to the list so that we can understand that we need to rewind the song
    # Передаємо значення "Back" у список , щоб можна було зрозуміти що треба перегорнути пісню назад
    list_flipping_song[0] = "Back"
    # If songs are currently being played in turn, then we do the code below
    # Якщо зараз граються пісні по черзі, то робимо код нижче
    if what_event[0] == "queue":
        # Check that the last song is currently playing
        # Перевіряємо щоб зараз грала остання пісня
        if label_for_show_name._text + ".mp3" == list_songs[-1]:
            # Check that the last song has finished playing
            # Перевіряємо щоб остання пісня закінчила грати
            if not pygame.mixer.music.get_busy():
                # Restart the thread
                # Запускаємо поток заново
                play_theread()
                # Pass the value "needback" to the list so that it is clear that the last song in the list has ended, and you can scroll back through the song
                # Передаємо до списку значення "needback" щоб було зрозуміло що закінчилась остання пісні у списку, і можна було перегорнути пісню назад
                previous_track[0] = "needback"
                

# Create a function to start a stream, with the function of playing songs one by one
# Створюємо функція для запуску потока , із функцією програвання пісень по черзці
def play_theread():
    # Create a thread
    # Створюємо поток
    play = Thread(target = play_song)
    # Start the thread
    # Запускаємо цей поток
    play.start()


#if event_pause = False this means there is a pause
#якщо event_pause = False це означає, що зараз стоїть пауза

# Create a function that pauses the song
# Створюємо функцію яка ставить на паузу пісню
def pause_music():
    #перевіряємо чи пауза,якщо знаходиться True означає що пауза не поставлена
    #check if a pause is set, if True is found it means that a pause is not set
    if event_pause.is_set(): 
        #if pause is pressed then we set false in event_pause and say that there is a pause now
        #якщо натиснули на паузу, то ставимо false в event_pause і кажемо, що зараз пауза
        event_pause.clear()  
        # Pause the music
        # Ставимо пісню на паузу
        pygame.mixer.music.pause() 


# Create a function that stops the song
# Створюємо функцію яка зупиняє пісню 
def stop_music():
    # Check if a pause is set, if it is True it means that a pause is not set
    # Перевіряємо чи пауза, якщо знаходиться True означає що пауза не поставлена
    if event_pause.is_set():
        # Stop the music
        # Зупиняємо пісню
        pygame.mixer.music.stop()
        #add 1 to the list so we can track whether a pause has been set
        #додаємо 1 до списку щоб могли відстежувати поставлена ​​пауза
        list_check_stop[0] += 1



# Create a frame to place the side buttons
# Створюємо фрейм , для розташування бокових кнопок
frame_bar = ctk.CTkFrame(app, width = 169 , height = 298 , fg_color = "#4cb7ce")
frame_bar.place(x = 268 , y = 83)


# setting up columns and rows for arranging buttons on the sidebar
# налаштування колонок і рядків для розміщення кнопок на бічній панелі
frame_bar.columnconfigure(0 , weight= 1) # | vertical columns
frame_bar.rowconfigure((0 , 1, 2, 3,), weight = 1) # - - - - -  horizontal columns

# Create button "start play music" 
# Створюємо кнопку "start play music"
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

# Place the button in the first (0) row and in the first (0) column, with a bottom indent of 10 px
# Розташовуємо кнопку у першому(0) рядку та у першій колонці(0) , з відступом сзнизу у 10 px
button_play.grid(row = 0 , column = 0 , pady = (0 , 10))

# Create button "skip music" 
# Створюємо кнопку "skip music"
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
# Place the button in the second (1) row and in the first column (0), with a 10 px indent
# Розташовуємо кнопку у другому(1) рядку та у першій колонці(0) , з відступом у 10 px
button_next_song.grid(row = 1 , column = 0 , sticky = "w", pady = 10)

# Create button "previous song" 
# Створюємо кнопку "previous song"
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
# Place the button in the second (1) row and in the first column (0), with a 10 px indent
# Розташовуємо кнопку у другому(1) рядку та у першій колонці(0) , з відступом у 10 px
button_prev_song.grid(row = 1 , column = 0 , sticky = "e", pady = 10)

# Create button "pause song" 
# Створюємо кнопку "pause song"
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
# Place the button in the third (2) row and in the first column (0), with a 10 px indent
# Розташовуємо кнопку у третьому(2) рядку та у першій колонці(0) , з відступом  у 10 px
button_pause.grid(row = 2 , column = 0 , pady = 10)

# Create button "stop song" 
# Створюємо кнопку "stop song"
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
# Place the button in the fourth (3) row and the first (0) column, with a top indent of 10 pixels
# Розташовуємо кнопку у четвертому(3) рядку та у першій колонці(0) , з відступом зверху у 10 пікселів
button_stop.grid(row = 3 , column = 0 , pady = (10 , 0))

# Create a label to display what music is playing now
# Створюємо лейбл для відображення, яка музика зараз грає
label_for_show_name = ctk.CTkLabel(master = app, text = "Пісня ще не грає" ,width = 160, height = 15 , font = ("Inter" , 16) , text_color = "#FFFFFF")
# Place the label in the main frame
# Розташовуємо лейбл у головному вікні
label_for_show_name.place(x = 270, y = 30)
