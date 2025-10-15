# operator_precedence.py - simple operator precedence evaluator for + - * / and parentheses
# This uses shunting-yard algorithm to transform to RPN then evaluate (demonstration of precedence)
import math, operator
ops = {'+':(1,operator.add), '-':(1,operator.sub), '*':(2,operator.mul), '/':(2,operator.truediv)}
def shunting_yard(expr):
    out=[]; stack=[]
    tokens = expr.replace('(',' ( ').replace(')',' ) ').split()
    for t in tokens:
        if t.isdigit(): out.append(t)
        elif t in ops:
            while stack and stack[-1] in ops and ops[stack[-1]][0]>=ops[t][0]:
                out.append(stack.pop())
            stack.append(t)
        elif t=='(':
            stack.append(t)
        elif t==')':
            while stack and stack[-1]!='(':
                out.append(stack.pop())
            stack.pop()
    while stack: out.append(stack.pop())
    return out

def eval_rpn(rpn):
    st=[]
    for t in rpn:
        if t.isdigit(): st.append(int(t))
        else:
            b=st.pop(); a=st.pop()
            st.append(ops[t][1](a,b))
    return st[0]

if __name__=='__main__':
    expr = "3 + 4 * ( 2 - 1 )"
    rpn = shunting_yard(expr)
    print('RPN:', rpn)
    print('Value:', eval_rpn(rpn))
