from ..utils import logger
from ..utils import globalvars


def handle(params: list[str]) -> int:
    """
    Funl function to check if the application is being run on the correct version

    params: str The version string
    """

    if len(params) != 1:
        logger.log_error("version", f"Invalid params: {params}")

    if params[0] != globalvars.VERSION:
        logger.log_error(
            "version",
            (
                "Running application on incorrect funl version. "
                f"Got: '{globalvars.VERSION}' Expected: '{params[0]}'"
            ),
        )

    return True
