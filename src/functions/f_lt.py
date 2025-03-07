from ..utils import logger


def handle(params: list[int]) -> int:
    """
    """

    if len(params) != 2:
        logger.log_error("gt", f"Invalid parameters: {params}")

    return params[0] < params[1]
