# Simple LL(1) parser for grammar: S -> a B
# B -> b | epsilon
# This is a toy demo with parsing table hardcoded
parsing_table = {
  ('S','a'): ['a','B'],
  ('B','b'): ['b'],
  ('B','$'): ['epsilon']
}
def parse(tokens):
  stack = ['S','$']
  tokens = tokens + ['$']
  i=0
  while stack:
    top = stack.pop()
    cur = tokens[i]
    if top==cur:
      i+=1
      if top=='$': return True
    elif top.isupper(): # nonterminal (simple check)
      prod = parsing_table.get((top,cur))
      if not prod: return False
      if prod[0]!='epsilon':
        for sym in reversed(prod):
          stack.append(sym)
    else:
      return False
  return False

if __name__=='__main__':
  print(parse(['a','b']))
  print(parse(['a']))
