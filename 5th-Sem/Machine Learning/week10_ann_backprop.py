
#!/usr/bin/env python3
import numpy as np
# Simple 2-layer neural network (1 hidden layer) trained with backprop on XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])
np.random.seed(1)
# network shape: 2 -> 2 -> 1
W1 = 2*np.random.random((2,2)) - 1
W2 = 2*np.random.random((2,1)) - 1
def sigmoid(x): return 1/(1+np.exp(-x))
def sigmoid_deriv(x): return x*(1-x)
for epoch in range(10000):
    l1 = sigmoid(np.dot(X, W1))
    l2 = sigmoid(np.dot(l1, W2))
    l2_error = y - l2
    if epoch % 2000 == 0:
        print("Error:", (l2_error**2).mean())
    l2_delta = l2_error * sigmoid_deriv(l2)
    l1_error = l2_delta.dot(W2.T)
    l1_delta = l1_error * sigmoid_deriv(l1)
    W2 += l1.T.dot(l2_delta)
    W1 += X.T.dot(l1_delta)
print("Final predictions:")
print(np.round(sigmoid(np.dot(sigmoid(np.dot(X,W1)),W2)),3))
