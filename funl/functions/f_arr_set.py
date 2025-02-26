from ..utils import logger


def handle(params: list[any]) -> list[any]:
    """
    Funl function to set an element of an already existing array.

    params: list[any]   param[0] has to be the array we want to set something of,
                        param[1] is the index of the element,
                        param[2] is the element that should be set

    Returns the updated array
    """

    if len(params) != 3:
        logger.log_error("arr_set", f"Invalid parameters for array set operation: {params}")

    value = params[0].copy()

    if params[1] < 0 or params[1] > len(params[0]) - 1:
        logger.log_error("arr_set", f"Index out of bounds: {params[1]} (max: {len(params[0] - 1)})")

    value[params[1]] = params[2]

    return value
