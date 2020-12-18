import copy
from functools import reduce
from itertools import groupby, permutations, product
import math
from operator import add, mul
import re
from typing import Callable, Dict, List, Set, Tuple

def evaluate(formula: List[str]) -> int:
  result = 0
  paren: List[int] = []
  op: List[str] = []
  for i in formula:
    if i == ' ':
      continue
    print(f'{result} , {paren}, {op}')
    if i == '+':
      op.append(i)
    elif i == '(' or i == '*':
      paren.append(result)
      op.append(i)
      result = 0
    elif i.isnumeric():
      if result == 0:
        result = int(i)
      elif op.pop() == '+':
        result += int(i)
      else:
        result *= int(i)
    else:
      closed = False
      while len(op) > 0:
        if closed and op[-1] == '(':
          break
        o = op.pop()
        if o == '(':
          closed = True
          if len(op) > 0 and op[-1] != '(':
            continue
          else:
            if paren[-1] == 0:
              paren.pop()
            break
        while len(paren) > 0 and paren[-1] == 0:
          paren.pop()
          continue
        if o == '+':
          result += int(paren.pop())
        else:
          if closed:
            op.append(o)
            break
          else:
            result *= int(paren.pop())
  while len(op) > 0:
    op.pop()
    result *= paren.pop()
  return result

if __name__ == "__main__":
  data = []
  with open('day18input') as f:
    data = [list(s.strip('\n')) for s in f.readlines()]
  for a in data:
    print(f'{"".join(a)}: {evaluate(a)}')
  print(sum(evaluate(f) for f in data))