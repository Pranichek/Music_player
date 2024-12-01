# Import the module for working with directories
# Імпортуємо модуль для роботи із директоріями
import os


# Function that returns the path to the image file
# Функція, яка повертає шлях до файлу зображення
def read_images(name_image: str):
   # Get the absolute path to the current file and dynamically pass the image name
   # Отримаємо абсолютний шлях до поточного файлу і динамічно передаємо назву зображення
   return os.path.abspath(__file__ + f"/../../../static/images/{name_image}.png")