from functools import reduce
from itertools import product
import math
from operator import add, mul
import re
from typing import Callable, Dict, List, Set, Tuple

def group(nums: List[int], sequence: List[int]) -> Dict[int, List[int]]:
  result: Dict[int, List[int]] = {}
  start = 0
  for i in range(len(nums) - len(sequence)):
    found = True
    for j in range(len(sequence)):
      if nums[i+j] != sequence[j]:
        found = False
        break
    if found:
      result[start] = nums[start:i+len(sequence)]
      start = i+len(sequence)
  result[start] = nums[start:-1]
  return result

def cycle(starting: List[int], target: int) -> int:
  array = []
  lastseen = {}
  lastnum = -1
  for i, n in enumerate(starting):
    lastseen[n] = [i]
    array += [n]
  lastnum = starting[-1]
  for i in range(len(starting), target):
    if len(lastseen[lastnum]) > 1:
      lastnum = lastseen[lastnum][0] - lastseen[lastnum][1]
    else:
      lastnum = 0
    lastseen[lastnum] = [i] if lastnum not in lastseen else [i] + lastseen[lastnum]
    array += [lastnum]
  for i, l in group(array, [0]).items():
    print(f'{i-2} {len(l)}: {l}')
  return lastnum

if __name__ == "__main__":
  nums: List[int] = []
  with open('day15input') as f:
    data = [s.strip('\n').split(',') for s in f.readlines()]
    nums = [int(x) for x in data[0]]

  print(cycle(nums, 300)) # part1