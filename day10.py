from functools import reduce
from operator import add, mul
from typing import List

if __name__ == "__main__":
  data = []
  with open('day10input') as f:
      data = [int(s) for s in f.readlines()]
  data.sort()
  gaps = [[a, b] for a, b in zip(data, data[1:]) if a+1 < b]
  print((len(data)-len(gaps)) * (len(gaps)+1))  # part 1
  data.insert(0, 0)
  edges = iter(data[:1] + reduce(add, gaps, []) + data[-1:])
  result = list(zip(edges, edges))
  print(reduce(mul, [(x[1]-x[0]-1)*(x[1]-x[0])/2+1 for x in result], 1)) # part 2
