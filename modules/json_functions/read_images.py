import os

def read_images(name_image: str):
   return os.path.abspath(__file__ + f"/../../../static/images/{name_image}.png")