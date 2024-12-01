# Import the module for working with directories
# Імпортуємо модуль для роботи із директоріями
import os 
# Import the module for working with JSON files
# Імпортуємо модуль для роботи з файлами JSON
import json


# Function that reads JSON file and returns its content
# Функція, яка читає файл JSON і повертає його вміст
def read_json(filename:str):
    # Get the absolute path to the current file and dynamically pass the filename
    # Отримаємо абсолютний шлях до поточного файлу та динамічно передайте назву файлу
    path_to_file = os.path.abspath(__file__ + f"/../../../static/{filename}")
    # Open the file in read mode
    # Відкриваємо файл у режимі читання
    with open(path_to_file, 'r') as file:
        # Read the content of the file and return it as a dictionary
        # Читаємо вміст файлу та повертаємо його як словник
        return json.load(file)