import customtkinter as ctk
from .main_frame import app
from ..jmages.get_images import image_add_song, image_del_song , image_mix_songs , image_sound_up , image_sound_down

#фрейм для нижней панели кнопок
frame_buttom = ctk.CTkFrame(master = app , width = 405 , height = 58 , fg_color = "#4cb7ce")
frame_buttom.place(x = 25 , y = 397)

#настройка колонок и рядков для растановки кнопок
frame_buttom.columnconfigure((0,1,2,3,4), weight = 1) #| | | | |
frame_buttom.rowconfigure(0 , weight = 1) # -

buttom_add = ctk.CTkButton(master = frame_buttom , text= "" ,width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_add_song , anchor = "center")
buttom_add.grid(row = 0 , column = 0 , padx = (0 , 25))

buttom_delete = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_del_song , anchor = "center")
buttom_delete.grid(row = 0 , column = 1 , padx = (0 , 25))

buttom_mix = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_mix_songs , anchor = "center")
buttom_mix.grid(row = 0 , column = 2, padx = (0 , 25))

button_sound_up = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_sound_up , anchor = "center")
button_sound_up.grid(row = 0 , column = 3 , padx = (0 , 25))

button_sound_down = ctk.CTkButton(master = frame_buttom , text= "" , width = 61 , height = 58, fg_color= "#bdbdbd", border_color = "black" , corner_radius = 20, border_width = 4, image = image_sound_down , anchor = "center")
button_sound_down.grid(row = 0 , column = 4)








