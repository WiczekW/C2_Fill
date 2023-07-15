import glob as gb


class LookProjectPath:
    def __init__(self, project):
        path_lev1 = gb.glob('\\\\dp.pekabex.poznan\\projekty*')
        path_lev2 = list()
        self.path_lev3 = list()
        self.folders = list()
        for i in path_lev1:
            multiple_path_lev2 = gb.glob(i + '\\' + project + '*\\Na produkcje')
            for j in multiple_path_lev2:
                path_lev2.append(j)

        for i in path_lev2:
            multiple_path_lev3 = gb.glob(i + '\\*')
            for j in multiple_path_lev3:
                self.path_lev3.append(j)


