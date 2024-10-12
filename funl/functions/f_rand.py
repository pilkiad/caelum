import random

from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to return a random integer between ranges of param[0] and param[1]

    params: list[int]   param[0] is min, param[1] is max
    """

    return random.randint(params[0], params[1])
