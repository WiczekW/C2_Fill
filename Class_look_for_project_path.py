import glob as gb


class LookProjectPath:
    def __init__(self, project):

    #temp solution to years
        year = 'a'
        if project[-1] == 'N':
            year = '2021'
        elif project[-1] == 'O':
            year = '2022'
        elif project[-1] == 'P':
            year = '2023'
        elif project[-1] == 'Q':
            year = '2024'

        path_lev1 = '\\\\dp.pekabex.poznan\\projekty' + year + '\\'
        path_lev2 = list()
        self.path_lev3 = []

        path_lev2_l = gb.glob(path_lev1 + project + '*')

        for i in path_lev2_l:
            i = i + '\\Na produkcje'
            path_lev2.append(i)

        for j in path_lev2:
            self.path_lev3.append(gb.glob(j + '\\*'))

        self.folders = list()

        if len(self.path_lev3) == 0:
            print('Nie odnaleziono folderu projektu')
            pr_path = input('Podaj ścieżkę do folderu tematu - ')
            multiple_path_lev3 = (gb.glob(pr_path + '\\Na produkcje\\*'))
            for i in multiple_path_lev3:
                self.path_lev3.append(i)
