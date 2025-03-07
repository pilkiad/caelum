from ..utils import logger


def handle(params: list[int]) -> int:
    """
    """

    for value in params:
        if value != True:
            return 0

    return 1
