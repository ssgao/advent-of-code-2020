import functools
from typing import Callable, Dict, List, Set

class Bag:
  def __init__(self):
    self.contains: Dict[str, int] = {}
    self.containedBy: Set[str] = set()

bags: Dict[str, Bag] = {}

data = []
with open('day7input') as f:
  data = [s.strip('.\n') for s in f.readlines()]

def build_graph():
  for d in data:
    name, ref = d.split(' contain ')
    name = name[:-5]
    if not name in bags:
      bags[name] = Bag()
    if not ref.startswith('no'):
      for bag in ref.split(', '):
        k, v = bag.split(' ', 1)
        v = v[:-4].strip()
        bags[name].contains[v] = int(k)
        if not v in bags:
          bags[v] = Bag()
        bags[v].containedBy.add(name)

def print_graph():
  for k, v in bags.items():
    print(f'{k}: {v.contains} & {v.containedBy}')

build_graph()

def find_contained_by(name: str, visited: Set[str]) -> int:
  count = 0
  for bag in bags[name].containedBy:
    if not bag in visited:
      count += 1
      visited.add(bag)
      count += find_contained_by(bag, visited)
  return count

print(find_contained_by('shiny gold', set())) # part 1

def find_contains(name: str) -> int:
  count = 0
  for k, v in bags[name].contains.items():
    count += v
    count += v * find_contains(k)
  return count

print(find_contains('shiny gold')) # part 2