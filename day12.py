from functools import reduce
from itertools import product
import math
from operator import add, mul
import re
from typing import Callable, Dict, List, Set, Tuple

def turn(direction: str, degree: int, xdir: int, ydir: int) -> (int, int):
  if direction == 'R':
    while degree > 0:
      degree -= 90
      if xdir == 1 and ydir == 0: # east
        xdir, ydir = 0, -1 # south
      elif xdir == 0 and ydir == -1: # south
        xdir, ydir = -1, 0 #west
      elif xdir == -1 and ydir == 0: # west
        xdir, ydir = 0, 1 # north
      else: # north
        xdir, ydir = 1, 0 # east
  else:
    while degree > 0:
      degree -= 90
      if xdir == 1 and ydir == 0: # east
        xdir, ydir = 0, 1 # north
      elif xdir == 0 and ydir == 1: # north
        xdir, ydir = -1, 0 #west
      elif xdir == -1 and ydir == 0: # west
        xdir, ydir = 0, -1 # south
      else: # south
        xdir, ydir = 1, 0 # east
  return (xdir, ydir)

def move(data: List[Tuple[str, int]]) -> int:
  x = y = 0
  xdir, ydir = 1, 0 # initial -> East
  for d in data:
    if d[0] == 'N':
      y += d[1]
    elif d[0] == 'S':
      y -= d[1]
    elif d[0] == 'E':
      x += d[1]
    elif d[0] == 'W':
      x -= d[1]
    elif d[0] == 'F':
      x += xdir * d[1]
      y += ydir * d[1]
    else:
      xdir, ydir = turn(d[0], d[1], xdir, ydir)
  return abs(x) + abs(y)


def turn_waypoint(direction: str, degree: int, xdir: int, ydir: int, wx: int, wy: int) -> (int, int, int, int):
  if direction == 'R':
    while degree > 0:
      degree -= 90
      wx, wy = wy, -wx
      if xdir == 1 and ydir == 0: # east
        xdir, ydir = 0, -1 # south
      elif xdir == 0 and ydir == -1: # south
        xdir, ydir = -1, 0 #west
      elif xdir == -1 and ydir == 0: # west
        xdir, ydir = 0, 1 # north
      else: # north
        xdir, ydir = 1, 0 # east
  else:
    while degree > 0:
      degree -= 90
      wx, wy = -wy, wx
      if xdir == 1 and ydir == 0: # east
        xdir, ydir = 0, 1 # north
      elif xdir == 0 and ydir == 1: # north
        xdir, ydir = -1, 0 #west
      elif xdir == -1 and ydir == 0: # west
        xdir, ydir = 0, -1 # south
      else: # south
        xdir, ydir = 1, 0 # east
  return (xdir, ydir, wx, wy)


def move_waypoint(data: List[Tuple[str, int]]) -> int:
  wx, wy = 10, 1
  x = y = 0
  xdir, ydir = 1, 0
  for d in data:
    if d[0] == 'N':
      wy += d[1]
    elif d[0] == 'S':
      wy -= d[1]
    elif d[0] == 'E':
      wx += d[1]
    elif d[0] == 'W':
      wx -= d[1]
    elif d[0] == 'F':
      x += wx * d[1]
      y += wy * d[1]
    else:
      xdir, ydir, wx, wy = turn_waypoint(d[0], d[1], xdir, ydir, wx, wy)
  return abs(x) + abs(y)

if __name__ == "__main__":
  data = []
  with open('day12input') as f:
      data = [(s[0], int(s[1:])) for s in f.readlines()]
  print(move(data))
  print(move_waypoint(data))

