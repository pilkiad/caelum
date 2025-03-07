from ..utils import logger


def handle(params: list[int]) -> int:
    """
    """

    if len(params) != 2:
        logger.log_error("div", f"Invalid params: {params}")

    try:
        value = params[0] / params[1]
    except:
        logger.log_error("div", f"Invalid params: {param}")

    return value
