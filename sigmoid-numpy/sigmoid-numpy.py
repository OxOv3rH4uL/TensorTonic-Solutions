import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    ans = []
    if type(x) == list:
        for i in x:
            if type(i) == list:
                k = []
                for j in i:
                    m = float((1)/(1+np.exp(-j)))
                    k.append(m)
                ans.append(k)
            else:
                a = float((1) / (1 + np.exp(-i)))
                ans.append(a)
        return ans
    else:
        return float((1)/(1+np.exp(-x)))