import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x*0.1))

def relu(x):
    return x if x >=0 else 0

def tanh(x):
    return 1.0 - 2/(1+math.exp(x+x))