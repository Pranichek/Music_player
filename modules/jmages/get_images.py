import customtkinter as ctk
from PIL import Image
from ..json_functions import read_images


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