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








    





