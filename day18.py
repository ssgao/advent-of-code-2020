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
    print(f'{result} , {paren}, {op}')
    if i == ' ':
      continue
    elif i == '+' or i == '*':
      op.append(i)
    elif i == '(':
      paren.append(result)
      op.append('+')
      result = 0
    elif i.isnumeric():
      operator = '+' if len(op) == 0 else op.pop()
      if operator == '+':
        result += int(i)
      else:
        result *= int(i)
    else:
      if len(op) > 0:
        if op.pop() == '+':
          result += int(paren.pop())
        else:
          result *= int(paren.pop())
  return result

if __name__ == "__main__":
  data = []
  with open('day18input') as f:
    data = [list(s.strip('\n')) for s in f.readlines()]
  print(sum(evaluate(f) for f in data))