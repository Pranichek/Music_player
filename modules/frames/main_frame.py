import customtkinter as ctk
from ..json_functions.read_json import read_json





dict = read_json(filename="config.json")

width = dict["main_frame"]["width"]
height = dict["main_frame"]["height"]
title = dict["main_frame"]["title"]
main_frame_color = dict["main_frame"]["fg_color"]

app = ctk.CTk(fg_color = main_frame_color)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_coordinate = (screen_width // 2) - (width // 2)
y_coordinate = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
app.title(title)

# #фрейм для демонстрации трэков которые добавлены
# frame_treks = ctk.CTkFrame(app, width = 233, height = 367 , corner_radius = 20 , border_color= "black", border_width= 4 , fg_color= "#bdbdbd")
# frame_treks.place(x = 14 , y = 15)


#создание label для название трэка который играет
label_track_name = ctk.CTkLabel(master = app, text = "назва треку що грає", font = ("Inter", 16),  width = 160 , height = 59, text_color = "white")
label_track_name.place(x = 270, y = 15)




    





