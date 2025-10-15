
#!/usr/bin/env python3
import numpy as np
import pandas as pd, sys

class Perceptron:
    def __init__(self, lr=0.1, epochs=1000):
        self.lr=lr; self.epochs=epochs
    def fit(self,X,y):
        Xb = np.column_stack([np.ones(len(X)),X])
        self.w = np.zeros(Xb.shape[1])
        for _ in range(self.epochs):
            for xi, yi in zip(Xb,y):
                pred = 1 if xi.dot(self.w)>=0 else 0
                self.w += self.lr*(yi-pred)*xi
    def predict(self,X):
        Xb = np.column_stack([np.ones(len(X)),X])
        return [1 if xi.dot(self.w)>=0 else 0 for xi in Xb]

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/binary_train.csv"
    df = pd.read_csv(path)
    X = df[['x1','x2']].values
    y = df['y'].values
    p = Perceptron(lr=0.1,epochs=20)
    p.fit(X,y)
    print("Weights:", p.w)
    print("Predictions on train:", p.predict(X))
