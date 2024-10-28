import customtkinter as ctk
from .main_frame import app

list_songs = []
#фрейм для демонстрации трэков которые добавлены
frame_treks = ctk.CTkFrame(app, width = 233, height = 367 , corner_radius = 20 , border_color= "black", border_width= 4 , fg_color= "#bdbdbd")
frame_treks.place(x = 14 , y = 15)