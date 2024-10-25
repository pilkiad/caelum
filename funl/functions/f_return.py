from ..utils import logger


def handle(params: list[any]) -> int:
    """
    Funl function to return out of a function scope

    params: list[any]   Whatever you want to return
    """

    if len(params) > 1:
        return params
    if len(params) == 1:
        return params[0]
