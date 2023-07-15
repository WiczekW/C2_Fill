from Func_data_gathering import gather_data
from Func_txt_read_basic import read_txt, attr_from_txt
import pandas as pd
import openpyxl

shortcut = input('Skrót tematu - ')

all_paths = gather_data(shortcut)
data_to_excel = pd.DataFrame(columns=attr_from_txt)

for i in all_paths.folders:
    for j in i.txt:
        new_elem = read_txt(j)
        data_to_excel = data_to_excel[data_to_excel['name'] != new_elem.iloc[0, 0]]
        data_to_excel = data_to_excel.merge(new_elem, how='outer')

data_to_excel.to_excel('C2_filler.xlsx')
print('Utworzono plik excel')



