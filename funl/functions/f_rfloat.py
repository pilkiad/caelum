import random

from ..utils import logger


def handle(params: list[float]) -> float:
    """
    Funl function to return a random float between ranges of param[0] and param[1]

    params: list[float]   param[0] is min, param[1] is max
    """

    try:
        return random.uniform(params[0], params[1])
    except:
        logger.log_error("rfloat", f"Invalid params: {params}")