from ..utils import logger


def handle(params: list[int]) -> int:
    """
    """

    odd = False

    for value in params:
        if value == True:
            odd = not odd

    return 1 if odd else 0
