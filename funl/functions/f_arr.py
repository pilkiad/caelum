from ..utils import logger


def handle(params: list[any]) -> list[any]:
    """
    Funl function to declare an array by return the only given parameter as
    an array of type any.

    params: list[any]   The data array.
                        Note that the first parameter defines the data type of
                        the array
    """

    if len(params) == 0:
        logger.log_error("arr", f"Missing parameters for array: {params}")

    value = []
    for i in range(1, len(params)):
        value.append(params[i])

    try:
        if params[0] == "bool":
            if any(val > 1 for val in value) or any(val < 0 for val in value):
                logger.log_error("arr", f"Boolean array contains invalid values: {params}")
            value = [int(val) for val in value]

        elif params[0] == "int":
            value = [int(val) for val in value]

        elif params[0] == "str":
            value = [str(val) for val in value]

        elif params[0] == "float":
            value = [float(val) for val in value]
    except:
        logger.log_error("arr", f"Error parsing array, are the types correct? {params}")

    return value
