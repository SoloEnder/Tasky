
from ..libs import path_maker
import json

def save_data(filepath: str, data):

    with open(filepath, "w") as f:
        json.dump(data, f)
    print("Data saved !")

def load_data(filepath: str):

    try:

        with open(filepath, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        print(f"Unable to load file data : file {filepath} not found !")
        return
    
    except json.JSONDecodeError:
        print(f"Unable to load data : file {filepath} corrupted !")
        return

    except PermissionError:
        print("Unable to load : Permission denied !")
        return

    except Exception as e:
        print("Unable to load file ! ", f"\n{e}")
        return

    else:
        return data
        