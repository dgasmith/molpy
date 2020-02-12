import numpy as np


def distance(point1, point2):
    """
    Calculate distance between two points.

    Parameters
    ----------
    point1 : array_like
        The first point.
    point2 : array_like
        The second point.

    Returns
    -------
    float
        The distance between point1 and point2. 
    """
    
    point1 = np.asarray(point1)    
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)    
