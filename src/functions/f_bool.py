from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to declare an boolean by return the only given parameter as
    int.

    params: list[int]   The value of the integer, has to be a list since textx
                        parses all parameters as arrays
                        (even if there is only one)
                        We consider booleans to be integers limited to 0 and 1
    """

    if len(params) != 1:
        logger.log_error("bool", f"Invalid params: {params}")

    try:
        value = int(params[0])

        if value != 0 and value != 1:
            logger.log_error("bool", f"Boolean may never be {params[0]}")
    except:
        logger.log_error("bool", f"Invalid param: {params[0]}")

    return value
