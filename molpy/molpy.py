"""
molpy.py
A really cool molecule manipulation package.

Handles the primary functions
"""

import numpy as np
from .util import distance


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


class Molecule:
    def __init__(self, symbols, geometry):
        self.symbols = np.asarray(symbols, dtype=str)
        self.geometry = np.asarray(geometry, dtype=float)

        if len(self.geometry.shape) != 2:
            self.geometry = self.geometry.reshape(-1, 3)

        if self.symbols.shape[0] != self.geometry.shape[0]:
            raise ValueError("Symbol and geometry length does not match!") 

    def distance(self, index1, index2):
        return distance(self.geometry[index1], self.geometry[index2])


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
