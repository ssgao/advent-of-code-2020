import functools
import re
from typing import Callable, Dict, List, Set, Tuple

def execute(instructions: List[Tuple[str, int]]) -> int:
  accumulator = 0
  executed_lines: Set[int] = set()
  current = 0
  while current < len(instructions):
    ins = instructions[current]
    if current in executed_lines:
      return -1
    else:
      executed_lines.add(current)
    if ins[0] == 'acc':
      accumulator += ins[1]
    elif ins[0] == 'jmp':
      current += ins[1]
      continue
    current += 1
  return accumulator

def deep_copy(data: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
  return [x[:] for x in data]

if __name__ == "__main__":
  data: List[Tuple[str, int]] = []
  with open('day8input') as f:
    tmp = [s.strip('\n').split(' ', 1) for s in f.readlines()]
    data = [(s[0], int(s[1])) for s in tmp]
  print(execute(data)) # part 1
  for i in range(len(data)):
    if data[i][0] == 'jmp':
      copy = deep_copy(data)
      copy[i] = ('nop', copy[i][1])
      if (result := execute(copy)) > -1:
        print(result)
    if data[i][0] == 'nop':
      copy = deep_copy(data)
      copy[i] = ('jmp', copy[i][1])
      if (result := execute(copy)) > -1:
        print(result)