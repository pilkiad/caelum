from ..utils import logger


def handle(params: list[str]) -> str:
    """
    Funl function to declare an string by return the only given parameter as
    str.

    params: list[str]   The value of the string, has to be a list since textx
                        parses all parameters as arrays
                        (even if there is only one)
    """

    if len(params) != 1:
        logger.log_error("str", f"Invalid params: {params}")

    try:
        value = str(params[0])
    except:
        logger.log_error("str", f"Invalid param: {params[0]}")

    return value
