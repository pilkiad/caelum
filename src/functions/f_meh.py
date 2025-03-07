from ..utils import logger


def handle(params: list[int]) -> int:
    """
    Funl function to declare an unassigned value "meh".
    Represented in python by None

    params: list[int]   Must be empty
    """

    if len(params) != 0:
        logger.log_error("meh", f"Invalid params: {params}")

    return "meh"
