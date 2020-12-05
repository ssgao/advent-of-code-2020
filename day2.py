data = []
with open('day2input') as f:
  data = [x.split(' ') for x in f.readlines()]

def isValidPart1(line: str) -> bool:
  min, max = [int(x) for x in line[0].split('-')]
  c = line[1].strip(':')
  counter = 0
  for x in line[2]:
    if x == c:
      counter += 1
    if counter > max:
      return False
  return counter >= min

print(sum(isValidPart1(x) for x in data))

def isValidPart2(line: str) -> bool:
  pos1, pos2 = [int(x)-1 for x in line[0].split('-')]
  c = line[1].strip(':')
  return (pos1 < len(line[2]) and line[2][pos1] == c) != (pos2 < len(line[2]) and line[2][pos2] == c)

print(sum(isValidPart2(x) for x in data))