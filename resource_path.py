import os
import sys

def resource_path(relative_path):
    """ Obtenir le chemin absolu du fichier après la compilation """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
