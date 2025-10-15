
#!/usr/bin/env python3
# Candidate-Elimination algorithm (simple implementation)
import csv, sys

def read_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        header=next(reader)
        data=[row for row in reader]
    return header, data

def more_general(a,b):
    more=False
    for x,y in zip(a,b):
        if x=='?': 
            if y!='?': more=True
        elif x!=y: 
            return False
    return more

def satisfies(h, x):
    for hv,xv in zip(h,x):
        if hv!='?' and hv!='0' and hv!=xv:
            return False
        if hv=='0': return False
    return True

def candidate_elimination(examples, attributes):
    n = len(attributes)-1
    # init
    G = [['?']*n
    ]
    S = [['0']*n]
    for ex in examples:
        x = ex[:n]
        label = ex[-1].strip().lower()
        if label=='yes':
            # remove G that don't satisfy x
            G = [g for g in G if satisfies(g,x)]
            # generalize S to satisfy x
            for i,s in enumerate(S):
                if not satisfies(s,x):
                    S[i] = [ (xj if sj=='0' else (sj if sj==xj else '?')) for sj,xj in zip(s,x) ]
            # remove more-general S
            S = [s for s in S if not any(more_general(s2,s) for s2 in S if s2!=s)]
        else:
            # remove S that satisfy x
            S = [s for s in S if not satisfies(s,x)]
            newG=[]
            for g in G:
                if satisfies(g,x):
                    # specialize g
                    for i,gi in enumerate(g):
                        if gi=='?':
                            for val in set(row[i] for row in examples):
                                if val!=x[i]:
                                    new = g.copy()
                                    new[i]=val
                                    newG.append(new)
                else:
                    newG.append(g)
            # keep only minimal generalizations
            G = [g for g in newG if not any(more_general(g2,g) for g2 in newG if g2!=g)]
    return S,G

if __name__=="__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "data/candidate_train.csv"
    attrs, examples = read_csv(path)
    S,G = candidate_elimination(examples, attrs)
    print("Final Specific boundary S:")
    for s in S: print(s)
    print("\nFinal General boundary G:")
    for g in G: print(g)
