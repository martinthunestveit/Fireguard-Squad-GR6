import random

def get_ttf():
    """Return a random time-to-fire value in minutes."""
    return random.randint(0, 30)

def get_traffic_light(ttf):
    """Return traffic light color based on time-to-fire."""
    if ttf < 5:
        return "red"
    elif 5 <= ttf <= 15:
        return "yellow"
    else:
        return "green"
