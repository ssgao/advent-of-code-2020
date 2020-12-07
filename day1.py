from typing import Dict, List, Set, Tuple

data: List[int] = []
with open('day1input') as b:
  data = [int(i) for i in b.readlines()]

# Part 1
knownNumbers: Set[int] = set()
for a in data:
  if 2020-a in knownNumbers:
    print(a * (2020-a))
    break
  else:
    knownNumbers.add(a)

# Part 2
numMap: Dict[int, Tuple[int, int]] = {}
for a in data:
  if a >= 2019:
    continue
  max = 2019-a
  for b in data:
    if b >= max-1:
      continue
    numMap[2020-a-b] = (a, b)

for a in data:
  if a in numMap:
    b, g = numMap[a]
    print(a * b * g)
    break