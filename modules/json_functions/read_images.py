import os


def read_images(name_image:str):
   path_to_image = os.path.abspath(__file__ + f"/../../../static/images/{name_image}.png")
   return path_to_image