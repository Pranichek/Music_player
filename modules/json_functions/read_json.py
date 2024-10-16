import os , json

def read_json(filename:str):
    path_to_file = os.path.abspath(__file__ + f"/../../../static/{filename}")
    with open(path_to_file, 'r') as file:
        return json.load(file)