from ..utils import logger


def handle(params: list[any]) -> list[any]:
    """
    Funl function to push an element to an already existing array.

    params: list[any]   param[0] has to be the array we want to push to,
                        param[1] is the element that should be pushed

    Returns the updated array
    """

    if len(params) < 2:
        logger.log_error("arr_push", f"Missing parameters for array push operation: {params}")

    value = params[0].copy()
    value.append(params[1])

    return value
