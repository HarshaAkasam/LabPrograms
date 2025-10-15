# const_propagation.py - simple constant propagation over a toy AST represented as list of assignments
# Example input: a = 2 ; b = a + 3 ; c = b + 4
def propagate(lines):
    consts = {}
    out = []
    for ln in lines:
        if '=' in ln:
            left, right = [x.strip() for x in ln.split('=',1)]
            # substitute known constants
            for k,v in consts.items():
                right = right.replace(k, str(v))
            try:
                val = eval(right)
                consts[left]=val
                out.append(f"{left} = {val}  # propagated")
            except Exception:
                out.append(f"{left} = {right}")
        else:
            out.append(ln)
    return out

if __name__=='__main__':
    code = ["a = 2", "b = a + 3", "c = b + 4", "d = c + x"]
    print('\n'.join(propagate(code)))
