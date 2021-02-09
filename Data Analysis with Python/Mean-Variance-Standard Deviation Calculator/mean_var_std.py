import numpy as np

def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    x = np.array(list)
    x = x.reshape(3,3)
    #print(x.mean(axis=0))
    calculations = {
      "mean" : [x.mean(axis=0).tolist(),x.mean(axis=1).tolist(),x.mean().tolist()],
      "variance": [x.var(axis=0).tolist(),x.var(axis=1).tolist(),x.var().tolist()],
      "standard deviation": [x.std(axis=0).tolist(),x.std(axis=1).tolist(),x.std().tolist()],
      'max': [x.max(axis=0).tolist(),x.max(axis=1).tolist(),x.max().tolist()],
      'min': [x.min(axis=0).tolist(),x.min(axis=1).tolist(),x.min().tolist()],
      'sum': [x.sum(axis=0).tolist(),x.sum(axis=1).tolist(),x.sum().tolist()]
    }
    return calculations