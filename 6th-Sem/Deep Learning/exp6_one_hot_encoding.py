# One-hot encoding demonstration for characters and words
from collections import defaultdict
def one_hot_chars(s):
    vocab = sorted(set(s))
    idx = {c:i for i,c in enumerate(vocab)}
    vecs = []
    for ch in s:
        v = [0]*len(vocab); v[idx[ch]]=1; vecs.append(v)
    return vecs, idx

def one_hot_words(text):
    words = text.split()
    vocab = sorted(set(words))
    idx = {w:i for i,w in enumerate(vocab)}
    vecs = []
    for w in words:
        v=[0]*len(vocab); v[idx[w]]=1; vecs.append(v)
    return vecs, idx

if __name__=='__main__':
    s = 'hello'
    print('one-hot chars sample mapping:', one_hot_chars(s)[1])
    text = 'this is a test this is fun'
    print('one-hot words sample mapping:', one_hot_words(text)[1])
