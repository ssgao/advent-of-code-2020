from itertools import product
import math
from operator import add, mul
from typing import List

def print_processed(data: List[str]):
  for d in data:
    print(d)

def move(i: int) -> int:
  return i if i == 0 else int(i+i/abs(i))

def is_occupied(data: List[str], i, j, idir, jdir, first) -> bool:
  while i+idir >= 0 and i+idir <= len(data)-1 and j+jdir >= 0 and j+jdir <= len(data[0])-1:
    return data[i+idir][j+jdir] == '#' if first or data[i+idir][j+jdir] != '.' else is_occupied(data, i, j, move(idir), move(jdir), first)
  return False

def process(data: List[str], occupiedlimit: int, first: bool) -> List[str]:
  processed: List[str] = [''] * len(data)
  for i in range(len(data)):
    tmp = list(data[i])
    for j in range(len(data[0])):
      if data[i][j] == '.':
        continue
      occupiedcount = sum(is_occupied(data, i, j, idir, jdir, first) for idir, jdir in product([-1, 0, 1], [-1, 0, 1]) if idir != 0 or jdir != 0)
      if occupiedcount == 0 and data[i][j] == 'L':
        tmp[j] = '#'
      elif data[i][j] == '#' and occupiedcount >= occupiedlimit:
        tmp[j] = 'L'
    processed[i] = ''.join(tmp)

  # print_processed(processed)
  return processed

def stablize(data: List[str], occupiedlimit: int, first: bool) -> int:
  next = process(data, occupiedlimit, first)
  while next != data:
    data, next = next, process(next, occupiedlimit, first)
  return sum(s.count('#') for s in data)

if __name__ == "__main__":
    data = []
    with open('day11input') as f:
        data = [s.strip('\n') for s in f.readlines()]
    print(stablize(data, 4, True))
    print(stablize(data, 5, False))
