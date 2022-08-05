from enum import Enum

import os


class Months(Enum):
    Jan = 0
    Feb = 1
    Mar = 2
    Apr = 3
    May = 4
    Jun = 5
    Jul = 6
    Aug = 7
    Sep = 8
    Oct = 9
    Nov = 10
    Dec = 11


def get_abspath(path):
    file_path = str(os.path.abspath(f'../images/{path}'))
    return os.path.abspath(file_path)
