# Importing module that can create Dekstop programs 
# Імпортуємо необхідний модуль для створення Dekstop програм
import customtkinter as ctk
# Import function that can reades json files
# Імпортуємо функція яка може читати json файли
from ..json_functions.json_reader import read_json

# Take a list of information for create window
# Беремо інформацію  про параметри віна із файлу config.json 
dict = read_json(filename="config.json")

print(dict)

# Take the main parameters from dict which we need to create main window
# Беремо потрібні параметри зі словаря dict для свторення вікна
width = dict["main_frame"]["width"]
height = dict["main_frame"]["height"]
title = dict["main_frame"]["title"]
main_frame_color = dict["main_frame"]["fg_color"]

# Create new window with parameters that we take from dict
# Створюємо головне вікно за параметрами які отримали
app = ctk.CTk(fg_color = main_frame_color)
# Use function that prohibits resizing the window
app.resizable(width  = False, height = False)

# Take a size of user screen to place window in the center
# Дізнаємося інформацію про розмір вікна користувача 
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Finds the center coord of screen
# Знаходимо центральні координати вікна , для розташування програми по центру
x_coordinate = (screen_width // 2) - (width // 2)
y_coordinate = (screen_height // 2) - (height // 2)


# Set the size of the empty window and place it in the center of the screen
# Задаємо розміру голоному вікну , та розташовуємо його по центру екрана
app.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

# Sets the title of the window
# Даємо назву вікну
app.title(title)








