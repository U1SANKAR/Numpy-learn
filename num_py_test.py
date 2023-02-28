import numpy as np
def Calculate(matrix):
    m = [matrix.mean(axis=1), matrix.mean(axis=0),matrix.mean()]
    v = [np.var(matrix,axis=1), np.var(matrix, axis=0), np.var(matrix)]
    s = [np.std(matrix,axis=1), np.std(matrix,axis=0), np.std(matrix)]
    m1 = [matrix.max(axis=1), matrix.max(axis=0), matrix.max()]
    m2 = [matrix.min(axis=1), matrix.min(axis=0), matrix.min()]
    s1 = [matrix.sum(axis=1), matrix.sum(axis = 0), matrix.sum()]
    d = [('mean',m),('variance',v),('standard deviation',s),('max',m1),('min',m2),('sum',s1)]
    return dict(d)

ele = list(map(int,input().split()))
M = np.array(ele).reshape(3,3)
print(Calculate(M))
