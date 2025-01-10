from ..utils import logger


def handle(params: list[any]) -> int:
    """
    Funl function to assert that two variables are the same and cause an exception
    if that was not the case

    params: list[any]   Expects two arguments that will be compared,
                        Optional assertion error text as third argument

    return              True if args are the same, error thrown if otherwise
    """
    # TODO - implement exception handling

    if len(params) != 2 and len(params) != 3:
        logger.log_error("assert", f"Invalid params: {params}")

    result = params[0] == params[1]

    if not result:
        if len(params) == 2:
            logger.log_error("assert", f"Assertion failed. Got: '{params[0]}' Expected: '{params[1]}'")
        else:
            logger.log_error("assert", f"Assertion failed. Got: '{params[0]}' Expected: '{params[1]}' Message: '{params[2]}'")

    return True
