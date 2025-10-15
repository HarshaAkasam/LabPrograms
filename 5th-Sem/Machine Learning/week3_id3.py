
#!/usr/bin/env python3
# Simple ID3 Decision Tree implementation (categorical)
import csv, sys, math
from collections import Counter, defaultdict

def read_csv(path):
    with open(path) as f:
        reader=csv.reader(f)
        header=next(reader)
        data=[row for row in reader]
    return header, data

def entropy(rows):
    counts=Counter([r[-1] for r in rows])
    total=len(rows)
    ent=0.0
    for c in counts.values():
        p=c/total
        ent -= p*math.log2(p)
    return ent

def info_gain(rows, attr):
    total=len(rows)
    vals=defaultdict(list)
    for r in rows:
        vals[r[attr]].append(r)
    remainder = sum((len(v)/total)*entropy(v) for v in vals.values())
    return entropy(rows)-remainder

def id3(rows, attrs):
    labels=[r[-1] for r in rows]
    if len(set(labels))==1:
        return labels[0]
    if not attrs:
        return Counter(labels).most_common(1)[0][0]
    gains=[(info_gain(rows,a),a) for a in attrs]
    _,best = max(gains)
    tree = { 'attr':best, 'nodes':{} }
    vals = set(r[best] for r in rows)
    for v in vals:
        subset=[r for r in rows if r[best]==v]
        if not subset:
            tree['nodes'][v]=Counter(labels).most_common(1)[0][0]
        else:
            new_attrs=[a for a in attrs if a!=best]
            tree['nodes'][v]=id3(subset,new_attrs)
    return tree

def classify(tree, sample):
    if isinstance(tree,str):
        return tree
    attr = tree['attr']
    val = sample[attr]
    if val in tree['nodes']:
        return classify(tree['nodes'][val], sample)
    else:
        # unseen value -> majority
        branches = tree['nodes'].values()
        if branches:
            return list(branches)[0] if isinstance(list(branches)[0], str) else list(branches)[0]
        return None

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/play_tennis.csv"
    header, data = read_csv(path)
    attrs = list(range(len(header)-1))
    tree = id3(data, attrs)
    print("Learned tree (recursive dict):")
    print(tree)
    # classify a sample
    sample = ['Sunny','Cool','High','Strong','Change']
    print("\nClassify sample", sample, "->", classify(tree, sample))
