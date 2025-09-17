# Créé par Admin, le 17/09/2025 en Python 3.7

import sys, os

def ressource_path(relative_path):
        try:
            base_path = sys.MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
