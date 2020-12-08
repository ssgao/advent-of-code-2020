from typing import List, Set, Tuple

def execute(instructions: List[Tuple[str, int]], fix_mode: bool) -> int:
  accumulator = 0
  executed_lines: Set[int] = set()
  current = 0
  while current < len(instructions):
    ins = instructions[current]
    if current in executed_lines:
      return -1 if fix_mode else accumulator
    else:
      executed_lines.add(current)
    if ins[0] == 'acc':
      accumulator += ins[1]
    elif ins[0] == 'jmp':
      current += ins[1]
      continue
    current += 1
  return accumulator

def swap(instructions: List[Tuple[str, int]], line: int) -> List[Tuple[str, int]]:
  copy = [x[:] for x in data] # deep copy
  copy[line] = ('nop' if copy[line][0] == 'jmp' else 'jmp', copy[line][1])
  return copy

def fix_program(instructions: List[Tuple[str, int]]) -> int:
  for i in range(len(instructions)):
    if instructions[i][0] == 'jmp' or instructions[i][0] == 'nop':
      copy = swap(instructions, i)
      if (result := execute(copy, True)) > -1:
        return result
  return result

if __name__ == "__main__":
  data: List[Tuple[str, int]] = []
  with open('day8input') as f:
    data = [(lambda x: (x[0], int(x[1])))(s.strip('\n').split(' ', 1)) for s in f.readlines()]
  print(execute(data, False)) # part 1
  print(fix_program(data))