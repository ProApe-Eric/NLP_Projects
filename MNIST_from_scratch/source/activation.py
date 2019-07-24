from math import exp
import numpy as np

def sigmoid(x):
    return 1 / (1 + exp(-x*1.0))

def relu(x):
    return x if x >=0 else 0.0

def tanh(x):
    return 1.0 - 2/(1+exp(x+x))

def relu6(x):
    return min(max(0,x),6)

def softmax(x):
    return exp(x) / exp(x).sum()

sigmoid = np.vectorize(sigmoid)
relu = np.vectorize(relu)
tanh = np.vectorize(tanh)
relu6 = np.vectorize(relu6)
exp = np.vectorize(exp)


