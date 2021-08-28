import json
import os
import sys


def add_user_to_blacklist(user_id: int):
    with open("blacklist.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].append(user_id)
    with open("blacklist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)


def remove_user_from_blacklist(user_id: int):
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(user_id)
    with open("blacklist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)


def load_config():
    if not os.path.isfile("config.json"):
        sys.exit("'config.json' not found! Please add it and try again.")
    else:
        with open("config.json") as file:
            return json.load(file)
