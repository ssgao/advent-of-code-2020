import functools
from typing import Callable, Dict, List, Set

class Bag:
  def __init__(self):
    self.contains: Dict[str, int] = {}
    self.containedBy: Set[str] = set()

bags: Dict[str, Bag] = {}

data = []
with open('day7input') as f:
  data = [s.strip('.\n').replace(' bags', '').replace(' bag', '') for s in f.readlines()]

def build_graph():
  for d in data:
    name, ref = d.split(' contain ')
    if name not in bags:
      bags[name] = Bag()
    if not ref.startswith('no'):
      for bag in ref.split(', '):
        k, v = bag.split(' ', 1)
        bags[name].contains[v] = int(k)
        if v not in bags:
          bags[v] = Bag()
        bags[v].containedBy.add(name)

build_graph()

def print_graph():
  for k, v in bags.items():
    print(f'{k}: {v.contains} & {v.containedBy}')

def find_contained_by(name: str, visited: Set[str]) -> int:
  count = 0
  for bag in bags[name].containedBy:
    if bag not in visited:
      visited.add(bag)
      count += 1 + find_contained_by(bag, visited)
  return count

print(find_contained_by('shiny gold', set())) # part 1

def find_contains(name: str) -> int:
  return sum(v + v * find_contains(k) for k, v in bags[name].contains.items())

print(find_contains('shiny gold')) # part 2