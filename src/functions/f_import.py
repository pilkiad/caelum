from ..utils import logger
from ..utils import grammar
from .. import parser


def handle(params: list[int]) -> int:
    """
    """

    if len(params) != 1:
        logger.log_error("import", f"Invalid params: {params}")

    logger.log_debug("import", f"Importing: {params[0]}")

    model = parser.file_to_model(f"src/{params[0]}.clm", grammar.grammar)

    return model
