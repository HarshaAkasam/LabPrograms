
#!/usr/bin/env python3
import numpy as np, pandas as pd, sys
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def remove_duplicates(df):
    return df.drop_duplicates()

def bias_variance_estimate(X,y,model_factory,iterations=50):
    # simple bootstrap-style estimate
    preds = []
    for i in range(iterations):
        idx = np.random.choice(len(X), len(X))
        model = model_factory()
        model.fit(X[idx], y[idx])
        preds.append(model.predict(X))
    preds = np.array(preds)
    mean_pred = preds.mean(axis=0)
    bias = np.mean((mean_pred-y)**2)
    variance = np.mean(preds.var(axis=0))
    return bias, variance

def cross_val(X,y,k=5):
    kf=KFold(n_splits=k,shuffle=True,random_state=1)
    mses=[]
    for train_idx,test_idx in kf.split(X):
        model=LinearRegression()
        model.fit(X[train_idx], y[train_idx])
        mses.append(mean_squared_error(y[test_idx], model.predict(X[test_idx])))
    return mses

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/bv_sample.csv"
    df = pd.read_csv(path)
    df2 = remove_duplicates(df)
    X = df2[['x']].values; y=df2['y'].values
    bias,var = bias_variance_estimate(X,y,lambda: LinearRegression(), iterations=100)
    print("Bias:", bias, "Variance:", var)
    print("Cross-val MSEs:", cross_val(X,y,5))
