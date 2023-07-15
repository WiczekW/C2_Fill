from Class_single_production_folder import SPF
from Class_look_for_project_path import LookProjectPath


def gather_data(prj):
    paths = LookProjectPath(prj)
    for i in paths.path_lev3:
        temp_obj = SPF(i)
        paths.folders.append(temp_obj)

#key to sort folders in list by creation date
    def sort_by_date(x):
        return x.creation_time

    paths.folders.sort(key=sort_by_date)
    return paths


