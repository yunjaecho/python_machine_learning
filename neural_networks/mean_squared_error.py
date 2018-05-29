import numpy as np

# 예1 : 2일 확률이 가장 높다고 추정함(0.6)
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(len(y))
# 정답은 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
print(len(t))

def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t)**2)

result = mean_squared_error(np.array(y), np.array(t))
print(result)   #0.0975

# 예2: 7일 확률이가장 높다고 추정함(0.6)
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
result = mean_squared_error(np.array(y), np.array(t))
print(result)   #0.5975

