
#!/usr/bin/env python3
import numpy as np, pandas as pd, sys

def sigmoid(z): return 1/(1+np.exp(-z))

def train(X,y,lr=0.1,epochs=1000):
    Xb = np.column_stack([np.ones(len(X)), X])
    theta = np.zeros(Xb.shape[1])
    for _ in range(epochs):
        preds = sigmoid(Xb.dot(theta))
        grad = Xb.T.dot(preds - y)/len(X)
        theta -= lr*grad
    return theta

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/logistic_regression.csv"
    df = pd.read_csv(path)
    X = df[['x1','x2']].values
    y = df['y'].values
    theta = train(X,y,lr=0.5,epochs=10000)
    print("Theta:", theta)
    # predict a sample
    xnew = np.array([1,2])
    Xb = np.concatenate(([1],xnew))
    print("Predicted prob:", sigmoid(Xb.dot(theta)))
