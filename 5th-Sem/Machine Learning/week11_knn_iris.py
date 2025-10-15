
#!/usr/bin/env python3
import pandas as pd, numpy as np
from collections import Counter
import sys, math

def read(path):
    df = pd.read_csv(path)
    return df

def euclid(a,b): return math.sqrt(((a-b)**2).sum())

def knn_predict(df, sample, k=3):
    X = df.iloc[:,:4].values
    y = df['species'].values
    dists = [ (euclid(x,sample),lab) for x,lab in zip(X,y) ]
    dists.sort(key=lambda x:x[0])
    top = [lab for _,lab in dists[:k]]
    return Counter(top).most_common(1)[0][0]

if __name__=="__main__":
    df = read("data/iris_small.csv")
    sample = df.iloc[0,:4].values
    pred = knn_predict(df, sample, k=3)
    print("Sample actual:", df.iloc[0,4])
    print("k-NN predicted:", pred)
