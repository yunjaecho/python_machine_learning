import numpy as np

def step_function(x):
    if x > 0:
        return 1
    else:
        return

print(step_function(0.4))

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

print(step_function2(np.array([1.0, 2.0])))