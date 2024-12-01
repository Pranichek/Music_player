# Import the customtkinter module to load images for the buttons
# Імпортуємо модуль customtkinter для того щоб завантажити зображення для кнопок
import customtkinter as ctk
# Import the PIL module to open images from the received paths, and convert the images to the image format for customtkinter
# Імопортуємо модуль PIL для того щоб відкривати зображення по отриманим шляхам , та перетворити зображення в формат зображень для customtkinter
from PIL import Image
# Import the read_images function from the json_functions module to get the paths to the images
# Імпортужмо функцію read_images з модуля json_functions, щоб отримати шляхи до зображень
from ..json_functions import read_images

# Create images for all buttons and set the size
# Створюємо зображення для усіх кнопок , та задаємо потрібні розміри
image_play = ctk.CTkImage(Image.open(read_images("play_button")) , size = (73 , 43))
image_next_song = ctk.CTkImage(Image.open(read_images("next_song_button")) , size = (30 , 20))
image_prev_song   = ctk.CTkImage(Image.open(read_images("prev_song_button")) , size = (30 ,20))
image_pause = ctk.CTkImage(Image.open(read_images("pause_button")) , size= (46 , 46))
image_stop = ctk.CTkImage(Image.open(read_images("stop_button")) , size = (42, 38))
image_add_song = ctk.CTkImage(Image.open(read_images("add_song_button")), size = (15 , 15))
image_del_song = ctk.CTkImage(Image.open(read_images("del_song_button")), size = (15 , 15))
image_mix_songs = ctk.CTkImage(Image.open(read_images("mix_songs_button")), size= (15 , 15))
image_sound_up = ctk.CTkImage(Image.open(read_images("sound_up_button")), size = (15 , 15))
image_sound_down = ctk.CTkImage(Image.open(read_images("sound_down_button")), size = (15 , 15))