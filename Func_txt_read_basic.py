import pandas as pd

attr_from_txt = ['name' ,'status', 'quantity', 'conc_vol', 'steel_mass']
def read_txt(path):

    with open(path, 'r') as file:
        temp_txt = file.read().split('§')
        temp_txt_ds = pd.Series(temp_txt)
        columns = attr_from_txt
        data_set = [temp_txt_ds[2] ,temp_txt_ds[22], temp_txt_ds[6], temp_txt_ds[7], temp_txt_ds[10]]
        output = pd.DataFrame(columns=columns, data=[data_set])
        return output


