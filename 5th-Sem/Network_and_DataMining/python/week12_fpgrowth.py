"""Week 12: FP-growth frequent pattern mining using fpgrowth_py package.
Usage: python week12_fpgrowth.py
"""
from fpgrowth_py import fpgrowth
def main():
    transactions = [
        ['milk','bread','butter'],
        ['bread','butter'],
        ['milk','bread'],
        ['bread'],
        ['milk','butter']
    ]
    patterns = fpgrowth(transactions, minsup=2)  # minsup as absolute count
    print('Frequent patterns (pattern -> support):')
    for pat, sup in patterns.items():
        print(pat, '->', sup)

if __name__=='__main__':
    main()
