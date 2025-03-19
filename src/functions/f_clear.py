import os

from ..utils import logger


def handle(params: list[int]) -> int:
    """
    """

    if len(params) != 0:
        logger.log_error("clear", f"Invalid params: {params}")


    os.system("clear" if os.name == "posix" else "cls")
