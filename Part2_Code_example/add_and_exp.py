
import numpy as np
from add import function_add_numbers


def function_add_and_exp(a: float, b: float) -> float:
    ab = function_add_numbers(a, b)
    e = np.exp(ab)
    return e
