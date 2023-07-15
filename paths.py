import glob as gb
import os.path

import pandas as pd




#First level of filepath

path_lev1 = gb.glob('C:\\Users\\Wik\\Desktop\\dp\\projekty*')
path_lev2 = list()
path_lev3 = list()
path_lev3_txt = list()

for i in path_lev1:
    multiple_path_lev2 = gb.glob(i + '\\*' + '\\Na produkcje')
    for j in multiple_path_lev2:
        path_lev2.append(j)


for i in path_lev2:
    multiple_path_lev3 = gb.glob(i + '\\*')
    for j in multiple_path_lev3:
        path_lev3.append(j)

for i in path_lev3:
    multiple_path_lev3 = gb.glob(i + '\\*')
    for j in multiple_path_lev3:
        path_lev3.append(j)

print(path_lev3)








#path_lev2 = gb.glob()