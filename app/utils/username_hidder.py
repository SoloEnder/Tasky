
import os

def remove_username(path: str):
    path = path.lower()
    username = os.path.expanduser("~")
    username = username.lower()
    path = path.replace(username, "~")
    return path