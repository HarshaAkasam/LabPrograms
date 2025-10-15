# Recursive descent parser for grammar:
# E -> T E'
# E' -> + T E' | - T E' | epsilon
# T -> F T'
# T' -> * F T' | / F T' | epsilon
# F -> (E) | num
import sys
tokens = []
pos = 0

def tokenize(s):
    return s.replace('(',' ( ').replace(')',' ) ').split()

def peek():
    return tokens[pos] if pos<len(tokens) else None

def match(tok):
    global pos
    if peek()==tok:
        pos+=1
        return True
    return False

def F():
    t = peek()
    if t=='(':
        match('('); val = E(); match(')'); return val
    elif t and t.isdigit():
        match(t); return int(t)
    else:
        raise Exception('Unexpected '+str(t))

def Tprime(left):
    if peek()=='*':
        match('*'); right=F(); return Tprime(left*right)
    if peek()=='/':
        match('/'); right=F(); return Tprime(left//right)
    return left

def T():
    left = F(); return Tprime(left)

def Eprime(left):
    if peek()=='+':
        match('+'); right=T(); return Eprime(left+right)
    if peek()=='-':
        match('-'); right=T(); return Eprime(left-right)
    return left

def E():
    left = T(); return Eprime(left)

if __name__=='__main__':
    s = "2 + 3 * (4 - 1)"
    tokens = tokenize(s)
    pos=0
    print('Expression:', s)
    print('Result:', E())
