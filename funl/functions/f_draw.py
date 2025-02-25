from ..utils import logger

import matplotlib.pyplot as plt
import numpy as np

def handle(params: list[list]) -> None:
    """
    Funl function to draw an arbitrary input array

    params: list[int]   The array to be drawn
    """

    if len(params) != 1:
        logger.log_error("draw", f"Invalid params: {params}")

    plt.figure(figsize=(6, 2))
    x = np.arange(len(params[0]))
    plt.bar(x, params[0], color="black")
    plt.xticks(x)
    plt.yticks(range(min(min(params[0]), 0), max(params[0]) + 1))
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title(f"{params[0]}")
    plt.show()
