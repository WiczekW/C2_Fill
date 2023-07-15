import os
import glob as gb

class SPF:
    def __init__(self, path):
        main_path = path
        self.creation_time = os.path.getmtime(path)
        self.txt = gb.glob(path + '\\*.txt')
        self.abs = gb.glob(path + '\\*.abs')
        self.dwg = gb.glob(path + '\\*.dwg')
        self.pdf = gb.glob(path + '\\*.pdf')

