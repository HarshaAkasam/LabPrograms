
#!/usr/bin/env python3
# Linear Regression: normal equation and gradient descent
import numpy as np, pandas as pd, sys

def read(path):
    df=pd.read_csv(path)
    X=df.iloc[:,:-1].values
    y=df.iloc[:,-1].values
    return X,y

def normal_eqn(X,y):
    Xb=np.column_stack([np.ones(len(X)),X])
    theta=np.linalg.pinv(Xb.T.dot(Xb)).dot(Xb.T).dot(y)
    return theta

def predict(theta,X):
    Xb=np.column_stack([np.ones(len(X)),X])
    return Xb.dot(theta)

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/linear_regression.csv"
    X,y = read(path)
    theta = normal_eqn(X,y)
    print("Theta (normal eqn):", theta)
    pred = predict(theta,X)
    print("MSE:", np.mean((pred-y)**2))
