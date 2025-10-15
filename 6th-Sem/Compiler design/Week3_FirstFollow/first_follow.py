# first_follow.py - compute FIRST and FOLLOW sets for a context-free grammar
# Grammar format: productions dict: A -> list of RHS (each RHS is list of symbols)
# Example grammar provided for demonstration.
from collections import defaultdict

G = {
  'E': [['T','E'']],
  "E'":[['+','T','E''],['epsilon']],
  'T':[['F','T'']],
  "T'":[['*','F','T''],['epsilon']],
  'F':[['(','E',')'],['id']]
}

NONTERMS = set(G.keys())
TERMS = set()

for A, rhss in G.items():
    for rhs in rhss:
        for sym in rhs:
            if sym not in G and sym != 'epsilon':
                TERMS.add(sym)

epsilon = 'epsilon'

def first(X, G, memo):
    if X in memo: return memo[X]
    res = set()
    if X not in G:
        res.add(X)
    else:
        for rhs in G[X]:
            if rhs==[epsilon]:
                res.add(epsilon)
                continue
            nullable = True
            for symbol in rhs:
                Fs = first(symbol, G, memo)
                res.update(Fs - {epsilon})
                if epsilon not in Fs:
                    nullable = False
                    break
            if nullable:
                res.add(epsilon)
    memo[X] = res
    return res

def compute_first_all(G):
    memo = {}
    for X in list(G.keys())+list(TERMS):
        first(X,G,memo)
    return memo

def compute_follow(G, start='E'):
    firsts = compute_first_all(G)
    follow = defaultdict(set)
    follow[start].add('$')
    changed = True
    while changed:
        changed = False
        for A, rhss in G.items():
            for rhs in rhss:
                trailer = set(follow[A])
                for symbol in reversed(rhs):
                    if symbol in G: # nonterminal
                        if not trailer.issubset(follow[symbol]):
                            follow[symbol].update(trailer)
                            changed = True
                        if 'epsilon' in firsts[symbol]:
                            trailer = trailer.union(firsts[symbol]-{'epsilon'})
                        else:
                            trailer = firsts[symbol]
                    else:
                        trailer = firsts[symbol] if symbol in firsts else {symbol}
    return dict(follow)

if __name__=='__main__':
    firsts = compute_first_all(G)
    print('FIRST sets:')
    for k in sorted(firsts.keys()):
        print(k, ':', firsts[k])
    print('\nFOLLOW sets:')
    follows = compute_follow(G)
    for k in sorted(follows.keys()):
        print(k, ':', follows[k])
