import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_next_song , image_prev_song , image_pause , image_stop, image_play
#оздание фрейм бара для боковой панели
frame_bar = ctk.CTkFrame(app, width = 169 , height = 298 , fg_color = "#4cb7ce")
frame_bar.place(x = 268 , y = 83)

#настройка колонок и рядков для растановки кнопок
frame_bar.columnconfigure(0 , weight= 1) # |
frame_bar.rowconfigure((0 , 1, 2, 3,), weight = 1) # - - - - - 


#создание кнопок для фрейма frame_bar
button_play = ctk.CTkButton(master= frame_bar , text = "",width = 169 , height = 60 , fg_color= "#bdbdbd" , border_color = "black", corner_radius= 20 , border_width= 4 , image= image_play , anchor = "center")
#в 44 строке делаем отступ только с низу с помощью такой стурктуры записи pady = (0 , 10)
button_play.grid(row = 0 , column = 0 , pady = (0 , 10))

button_next_song = ctk.CTkButton(master= frame_bar ,text= "" ,width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4 , image=image_next_song , anchor = "center")
button_next_song.grid(row = 1 , column = 0 , sticky = "w", pady = 10)

button_prev_song = ctk.CTkButton(master = frame_bar, text= "" ,width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image= image_prev_song, anchor="center")
button_prev_song.grid(row = 1 , column = 0 , sticky = "e", pady = 10)

button_pause = ctk.CTkButton(master = frame_bar , text = "", width = 169, height = 60 , fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_pause , anchor = "center")
button_pause.grid(row = 2 , column = 0 , pady = 10)

button_stop = ctk.CTkButton(master = frame_bar , text = "", width = 169 , height = 60 , fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_stop , anchor= "center")
#в 57 строке делаем отступ только сверху от кнопки с помощью такой записи pady = (10 , 0)
button_stop.grid(row = 3 , column = 0 , pady = (10 , 0))