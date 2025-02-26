from ..utils import logger


def handle(params: list[int]) -> int:
    """
    """

    for value in params:
        if value != params[0]:
            return 0

    return 1
