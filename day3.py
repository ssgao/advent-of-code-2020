import functools

data = []
with open('day3input') as f:
    data = [x.strip() for x in f.readlines()]

def arborealStops(right: int, down: int) -> int:
  width = len(data[0])
  x, counter = 0, 0
  for y in range(0, len(data), down):
      if data[y][x] == '#':
          counter += 1
      x = (x + right) % width
  return counter

print([arborealStops(*x) for x in [(1,1),(3,1),(5,1),(7,1),(1,2)]])
print(functools.reduce(lambda a, b: a*b, [arborealStops(*x) for x in [(1,1),(3,1),(5,1),(7,1),(1,2)]]))