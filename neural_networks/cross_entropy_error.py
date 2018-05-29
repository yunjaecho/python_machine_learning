import numpy as np

# 예1 : 2일 확률이 가장 높다고 추정함(0.6)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(len(y))
# 정답은 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
print(len(t))

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

result = cross_entropy_error(np.array(y), np.array(t))
print(result)   #0.510825457099

# 예2: 7일 확률이가장 높다고 추정함(0.6)
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
result = cross_entropy_error(np.array(y), np.array(t))
print(result)   #2.30258409299

