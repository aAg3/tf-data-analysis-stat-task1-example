import pandas as pd
import numpy as np


chat_id = 348708372 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    o = np.sqrt(np.log(1 + x.var() / x.mean() ** 2)) 
    m = np.log(x.mean() / np.sqrt(1 + x.var() / x.mean() ** 2)) 

    return np.exp(m - o ** 2 / 2) - 107
