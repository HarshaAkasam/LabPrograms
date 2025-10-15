# loop_unroll.py - a tiny source-to-source transformer that unrolls simple for loops of form:
# for i in range(N): body
# It looks for markers and duplicates body unroll_factor times (demo)
import re, sys

sample = '''for i in range(3):
    print(i)
'''

def unroll(code, factor=2):
    # VERY simplistic: only handles single-line body indented by 4 spaces
    m = re.search(r'for\s+(\w+)\s+in\s+range\((\d+)\):\n(\s+)(.+)\n', code)
    if not m: return code
    var, N, indent, body = m.group(1), int(m.group(2)), m.group(3), m.group(4)
    out = ''
    for i in range(int(N)):
        for k in range(factor):
            out += indent + body + '\n'
    return out

if __name__=='__main__':
    print('Original:\n', sample)
    print('Unrolled:\n', unroll(sample, factor=3))
