import json


import json
import os

def load_channel_ids(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Loaded JSON data: {data}")  # Debug: Print loaded JSON
        return data.get("channels_lst", [])
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

#def load_channel_ids(file_path):
#    try:
#        with open(file_path, 'r') as file:
#            data = json.load(file)
#            print(f"Loaded JSON data: {data}")  # Debug: Print loaded JSON
#        return data.get("channels_lst", [])
#    except FileNotFoundError:
#        print(f"Error: File not found at {file_path}")

    
def save_channel_list(file_path, channel_lst):
    with open(file_path, "w") as file:
        json.dump({"channels_lst": channel_lst}, file, indent=4)