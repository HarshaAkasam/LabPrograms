"""Week 11: Apriori frequent itemset mining using mlxtend.
Usage: python week11_apriori.py
"""
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def main():
    # Example transactional dataset: list of transactions
    transactions = [
        ['milk','bread','butter'],
        ['bread','butter'],
        ['milk','bread'],
        ['bread'],
        ['milk','butter']
    ]
    # one-hot encode
    items = sorted({item for t in transactions for item in t})
    df = pd.DataFrame([{item:(item in t) for item in items} for t in transactions])
    print('One-hot encoded:\n', df)
    freq = apriori(df, min_support=0.4, use_colnames=True)
    print('Frequent itemsets:\n', freq)
    rules = association_rules(freq, metric='confidence', min_threshold=0.7)
    print('Association rules:\n', rules)

if __name__=='__main__':
    main()
