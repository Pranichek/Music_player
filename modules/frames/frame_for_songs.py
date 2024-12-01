# Import module that can create Dekstop programs 
# Імпортуємо необхідний модуль для створення Dekstop програм
import customtkinter as ctk
# Import the main frame in the ptoject , where we place all another frames with objects
# Імпортуємо головний фрейм у проєкті, де розташовуємо усі інші фрейми із об'єктами
from .main_frame import app

# Create list for loaded songs
# Створюємо список де зберігаються усі завантажені пісні 
list_songs = []


# Create frame where place buttons with name songs
# Створюємо фрейм де будуть розташовуватися кнопки із назвами пісень
frame_treks = ctk.CTkScrollableFrame(app, 
                           width = 200, 
                           height = 318 , 
                           corner_radius = 20 , 
                           border_color= "black", 
                           border_width= 4 , 
                           fg_color= "#bdbdbd")
# Place it in the main frame
# Розташовуємо його на головному вікні
frame_treks.place(x = 14 , y = 15)