import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    return np.cos(x[1])

def f3(x: np.ndarray) -> np.ndarray:
    return np.exp(x[2])

def f4(x: np.ndarray) -> np.ndarray:
    return np.log(x[3]) 

def f5(x: np.ndarray) -> np.ndarray:
    return np.sqrt(x[4])    

def f6(x: np.ndarray) -> np.ndarray:
    return np.abs(x[5]) 

def f7(x: np.ndarray) -> np.ndarray:
    return x[6]**2

def f8(x: np.ndarray) -> np.ndarray:
    return x[7]**3


