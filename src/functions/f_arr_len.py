from ..utils import logger


def handle(params: list[any]) -> list[any]:
    """
    """

    if len(params) != 1:
        logger.log_error("arr_len", f"Invalid parameters: {params}")

    return len(params[0])
