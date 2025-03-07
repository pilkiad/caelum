from ..utils import logger


def handle(params: list[any]) -> int:
    """
    Funl function to return out of a function scope

    params: list[any]   Whatever you want to return
    """

    if len(params) > 1:
        logger.log_debug("return", f"<- {params}")
        return params
    if len(params) == 1:
        logger.log_debug("return", f"<- {params[0]}")
        return params[0]
