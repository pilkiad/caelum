import random

from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to return a random integer between ranges of param[0] and param[1]

    params: list[int]   param[0] is min, param[1] is max
    """

    try:
        return random.randint(params[0], params[1])
    except:
        logger.log_error("rint", f"Invalid params: {params}")