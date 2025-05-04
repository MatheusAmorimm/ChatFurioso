import json
import random

def get_curiosities():
    with open("data/curiosities.json", "r", encoding="utf-8") as file:
        curiosities = json.load(file)
    return random.choice(curiosities)