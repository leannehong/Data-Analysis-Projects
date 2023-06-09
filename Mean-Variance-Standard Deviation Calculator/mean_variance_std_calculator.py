import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must have nine numbers.')
    else:
        matrix = np.array(list).reshape(3, 3)
    
    mean = [(matrix.mean(axis = 0).tolist()),
            (matrix.mean(axis = 1).tolist()),
            (matrix.flatten().mean())]
    var = [(matrix.var(axis = 0).tolist()),
           (matrix.var(axis = 1).tolist()),
           (matrix.flatten().var())]
    std = [(matrix.std(axis = 0).tolist()),
           (matrix.std(axis = 1).tolist()),
           (matrix.flatten().std())]
    maxs = [(matrix.max(axis = 0).tolist()),
           (matrix.max(axis = 1).tolist()),
           (matrix.flatten().max())]
    mins = [(matrix.min(axis = 0).tolist()),
           (matrix.min(axis = 1).tolist()),
           (matrix.flatten().min())]
    sums = [(matrix.sum(axis = 0).tolist()),
           (matrix.sum(axis = 1).tolist()),
           (matrix.flatten().sum())]
    
    calc = {
        "mean": mean,
        "variance": var,
        "standard deviation": std,
        "max": maxs,
        "min": mins,
        "sum": sums,
    }

    return calc


print(calculate([0,1,2,3,4,5,6,7,8]))