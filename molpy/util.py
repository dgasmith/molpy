import numpy as np


def distance(point1, point2):
    
    point1 = np.asarray(point1)    
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)    
