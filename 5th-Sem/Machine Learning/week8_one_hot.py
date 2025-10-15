
#!/usr/bin/env python3
import pandas as pd
def one_hot(df, columns):
    return pd.get_dummies(df, columns=columns)
if __name__=="__main__":
    df = pd.DataFrame({'color':['red','blue','green','red'],'size':['S','M','L','S']})
    print("Original:\n", df)
    print("\nOne-hot encoded:\n", one_hot(df,['color']))
