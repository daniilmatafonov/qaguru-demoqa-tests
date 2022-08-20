from enum import Enum
from pathlib import Path

import tests


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


def get_resources(relative_path):
    return (
        Path(tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )

