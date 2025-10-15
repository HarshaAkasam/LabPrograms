
#!/usr/bin/env python3
import pandas as pd
from collections import defaultdict
def label_encode(series):
    mapping = {v:i for i,v in enumerate(sorted(series.unique()))}
    return series.map(mapping), mapping

def target_encode(df, col, target):
    means = df.groupby(col)[target].mean()
    return df[col].map(means.to_dict())

if __name__=="__main__":
    df = pd.DataFrame({'city':['A','B','A','C','B'],'y':[1,0,1,1,0]})
    le,m = label_encode(df['city'])
    print("Label encoded:\n", le.to_list(), "mapping:", m)
    print("Target encoded:\n", target_encode(df,'city','y').to_list())
