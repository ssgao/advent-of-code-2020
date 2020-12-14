from functools import reduce
from itertools import product
import math
from operator import add, mul
import re
from typing import Callable, Dict, List, Set, Tuple

def earliest(time: int, buses: List[Tuple[int, int]]) -> int:
  return math.prod(min((math.ceil(time / b) * b - time, b) for b in [bus[1] for bus in buses]))

# def earliest2(buses: List[Tuple[int, int]]) -> int:
#   current = buses[0][1]
#   while True:
#     found = True
#     for i, b in buses:
#       if (current + i) % b != 0:
#         found = False
#         break
#     if found:
#       return current
#     current += buses[0][1]
#   return 0


if __name__ == "__main__":
  time = 0
  buses = []
  with open('day13input') as f:
    data = [s.strip('\n') for s in f.readlines()]
    time = int(data[0])
    buses = [(i, int(b)) for i, b in enumerate(data[1].split(',')) if b != 'x']
  print(earliest(time, buses))
