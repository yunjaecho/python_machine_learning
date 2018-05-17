import numpy as np

A = np.array([[1,2], [3,4]])  # 2 * 2
B = np.array([[5,6], [7,8]])  # 2 * 2
C = np.dot(A, B)
print(C)

A = np.array([[1,2,3], [4,5,6]])      # 2*3
B = np.array([[1,2], [3,4], [5,6]])   # 3*2
C = np.dot(A, B)
print(C)


A = np.array([[1,2], [3,4], [5,6]])  # 3 * 2
B = np.array([7,8])                  # 2
C = np.dot(A, B)
print(C)
