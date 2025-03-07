from ..utils import logger


def handle(params: list[float]) -> float:
    """
    Funl function to declare an floating point value by return the only given
    parameter as float.

    params: list[float] The value of the float, has to be a list since textx
                        parses all parameters as arrays
                        (even if there is only one)
    """

    if len(params) != 1:
        logger.log_error("float", f"Invalid params: {params}")

    try:
        value = float(params[0])
    except:
        logger.log_error("float", f"Invalid param: {params[0]}")

    return value
