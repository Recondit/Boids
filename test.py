import numpy as np


class Vector:
    def __init__(A,B):
        A.self = A
        B.self = B
    def add(A,B):
        return (A[0]+B[0] , A[1] + B[1])
    def subtract(A,B):
        return (A[0]-B[0] , A[1] - B[1])


print(Vector.add((1,3) , (4,6)))
print(np.random.random(2))