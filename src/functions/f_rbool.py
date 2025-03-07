import random

from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to return a random integer between ranges of param[0] and param[1]

    params: list[int]   param[0] is min, param[1] is max
    """

    if len(params) != 0:
        logger.log_error("rbool", f"Random bool does not take arguments: {params}")

    return random.randint(0, 1)