import copy
from itertools import product
from typing import List

def process(pocket: List[List[List[List[bool]]]]) -> List[List[List[List[bool]]]]:
  new_pocket: List[List[List[List[bool]]]] = copy.deepcopy(pocket)
  for w in range(1, len(pocket)-1):
    for z in range(1, len(pocket[0])-1):
      for y in range(1, len(pocket[0][0])-1):
        for x in range(1, len(pocket[0][0][0])-1):
          activecount = sum([pocket[w+i][z+j][y+k][x+l] for i,j,k,l in product([-1,0,1], repeat=4) if (i,j,k,l) != (0,0,0,0)])
          new_pocket[w][z][y][x] = activecount == 3 or (pocket[w][z][y][x] and activecount == 2)
  return new_pocket

def cycle(pocket: List[List[List[List[bool]]]], times: int) -> int:
  for _ in range(times):
    pocket = process(pocket)
    # plot(pocket)
  return sum(x for x in sum(sum(sum(pocket, []), []), []))

def pad(starting: List[List[bool]], times: int, enable4d: bool) -> List[List[List[List[bool]]]]:
  addition = 2 * times
  pocket: List[List[List[List[bool]]]] = []
  for _ in range(addition+1 if enable4d else 3):
    pz = []
    for _ in range(addition+1):
      py = []
      for _ in range(addition+len(starting)):
        py.append([False] * (addition+len(starting[0])))
      pz.append(py)
    pocket.append(pz)
  mw = int(len(pocket) / 2)
  mz = int(len(pocket[0]) / 2)
  sx = sy = int(len(pocket[0][0]) / 2) - int(len(starting[0]) / 2)
  for i, j in product(list(range(len(starting[0]))), repeat=2):
    pocket[mw][mz][sy+i][sx+j] = starting[i][j]
  return pocket

def plot(pocket: List[List[List[List[bool]]]]):
  for w in range(len(pocket)):
    for z in range(len(pocket[0])):
      print(f'z={z-int(len(pocket[0])/2)}, w={w-int(len(pocket)/2)}')
      for y in range(len(pocket[0][0])):
        print(''.join('#' if x else '.' for x in pocket[w][z][y]))
      print()

if __name__ == "__main__":
  data: List[List[bool]] = []
  times: int = 6
  with open('day17input') as f:
    data = [[f == '#' for f in list(d)] for d in [s.strip('\n') for s in f.readlines()]]
  pocket = pad(data, times+1, False)
  print(cycle(pocket, times)) # part 1
  pocket = pad(data, times+1, True)
  print(cycle(pocket, times)) # part 2