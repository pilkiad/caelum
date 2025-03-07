from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to substract multiple integers.

    params: list[int]   The integers to be substracted
    """

    if len(params) <= 1:
        logger.log_error("sub", f"Invalid params: {params}")

    result = params[0]

    for i in range(0, len(params)):
        if i == 0:
            continue
        try:
            value = int(params[i])
        except:
            logger.log_error("sub", f"Invalid param: {param}")

        result -= value

    return result
