import numpy
from typing import List


def generate_integers(start: int, stop: int, step: int) -> List[int]:
    return numpy.arange(start, stop, step, dtype=int)


# This is for checking that code coverage will be <100%.
# def generate_something() -> bool:
#     return True
