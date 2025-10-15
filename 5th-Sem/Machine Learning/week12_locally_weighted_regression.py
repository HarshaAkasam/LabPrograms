
#!/usr/bin/env python3
import numpy as np, pandas as pd, matplotlib.pyplot as plt, sys
def lwlr(test_point, X, y, tau=0.5):
    Xb = np.column_stack([np.ones(len(X)), X])
    test = np.concatenate(([1], test_point))
    W = np.diag(np.exp(-np.sum((X - test_point)**2, axis=1)/(2*tau**2)))
    theta = np.linalg.pinv(Xb.T.dot(W).dot(Xb)).dot(Xb.T).dot(W).dot(y)
    return test.dot(theta)

if __name__=="__main__":
    df = pd.read_csv("data/lwlr_sample.csv")
    X = df[['x']].values
    y = df['y'].values
    xs = np.linspace(X.min(), X.max(), 100)
    ys = [lwlr([xx], X, y, tau=0.3) for xx in xs]
    plt.scatter(X, y)
    plt.plot(xs, ys)
    plt.title("Locally Weighted Linear Regression")
    plt.savefig("lwlr_plot.png")
    print("Saved lwlr_plot.png")
