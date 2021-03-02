import numpy as np

def calculate(l):
    if(len(l) == 9):
        calculations = {}
        a = np.array(l); a = a.reshape(3,3)
        m = [list(np.mean(a,axis = 0)), list(np.mean(a,axis = 1)), np.mean(a)]
        v = [list(np.var(a, axis = 0)), list(np.var(a,axis=1)), np.var(a)]
        sd = [list(np.std(a,axis=0)), list(np.std(a,axis=1)), np.std(a)]
        ma = [list(np.max(a,axis=0)), list(np.max(a,axis=1)), np.max(a)]
        mi = [list(np.min(a,axis=0)), list(np.min(a,axis=1)), np.min(a)]
        s = [list(np.sum(a,axis=0)), list(np.sum(a,axis=1)), np.sum(a)]
        calculations = {
            "mean" : m,
            "variance" : v,
            "standard deviation":sd,
            "max":ma,
            "min":mi,
            "sum":s
            }
        return calculations

    else:
        raise ValueError("List must contain nine numbers.")


