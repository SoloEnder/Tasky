from pathlib import Path
import getpass

def remove_username(path):
    # Convertit en string
    path_str = str(path)

    # Nom de l’utilisateur actuel
    username = getpass.getuser()

    # Remplace uniquement le nom d'utilisateur dans les chemins
    return path_str.replace(f"/home/{username}", "~")
