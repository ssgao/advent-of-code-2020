from functools import reduce
from itertools import product
import math
from operator import add, mul
import re
from typing import Callable, Dict, List, Set, Tuple

class Program:
  def __init__(self, mask: str, mems: List[Tuple[int, int]]):
    self.mask = mask
    self.mems = mems

def mask_it(mask: str, value: str) -> int:
  return int(''.join([v if m == 'X' else m for m, v in zip(mask, value)]), base=2)

def pad(value: str) -> str:
  return ''.join((value[::-1] + '0' * (36 - len(value)))[::-1])

def process(program: List[Program]) -> int:
  result: Dict[int, int] = {}
  for p in program:
    for m in p.mems:
      result[m[0]] = mask_it(p.mask, pad(bin(m[1])[2:]))
  return sum(result.values())

def apply_mask(template: List[str], indicies: List[int], values: List[int]) -> List[int]:
  if len(indicies) == len(values):
    for i, v in zip(indicies, values):
      template[i] = str(v)
    return [int(''.join(template), base=2)]
  else:
    return apply_mask(template, indicies, values + [0]) + apply_mask(template, indicies, values + [1])

def mask_it2(mask: str, value: str) -> Set[int]:
  result = [v if m == '0' else m for m, v in zip(mask, value)]
  xs = [i for i, x in enumerate(result) if x == 'X']
  return set(apply_mask(result, xs, []))

def process2(program: List[Program]) -> int:
  result: Dict[int, int] = {}
  for p in program:
    for m in p.mems:
      for k in mask_it2(p.mask, pad(bin(m[0])[2:])):
        result[k] = m[1]
  #     print(f'{m[0]}: {result[m[0]]}')
  # print(result.values())
  return sum(result.values())

if __name__ == "__main__":
  program = []
  with open('day14input') as f:
    data = [s.strip('\n') for s in f.readlines()]
    mask = ''
    mems = []
    for d in data:
      key, value = d.split(' = ')
      if key == 'mask':
        if len(mems) > 0:
          program.append(Program(mask, mems))
          maks = ''
          mems = []
        mask = value
      else:
        mems.append((int(key[4:-1]), int(value)))
    program.append(Program(mask, mems))
  print(process(program))
  print(process2(program))
