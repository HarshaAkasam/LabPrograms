
#!/usr/bin/env python3
# FIND-S algorithm implementation
import csv
import sys

def read_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def find_s(examples, attributes):
    # target expected in last column as 'Yes'/'No'
    n_attr = len(attributes)-1
    hypothesis = ['0']*n_attr
    for ex in examples:
        if ex[-1].strip().lower()=='yes':
            if hypothesis[0]=='0':
                hypothesis = ex[:n_attr].copy()
            else:
                for i in range(n_attr):
                    if hypothesis[i]!=ex[i]:
                        hypothesis[i]='?'
    return hypothesis

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/finds_train.csv"
    header, data = read_csv(path)
    hyp = find_s(data, header)
    print("Attributes:", header[:-1])
    print("Most specific hypothesis (FIND-S):")
    print(hyp)
