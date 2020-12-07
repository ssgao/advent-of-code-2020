from typing import Dict, Set

data = []
with open('day7input') as f:
  data = [s.strip('.\n').replace(' bags', '').replace(' bag', '') for s in f.readlines()]

class Bag:
  def __init__(self):
    self.contains: Dict[str, int] = {}
    self.containedBy: Set[str] = set()

bags: Dict[str, Bag] = {}

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
  print(*(f'{k}: {v.contains} & {v.containedBy}\n' for k, v in bags.items()))

def find_contained_by(name: str, visited: Set[str]) -> int:
  visited.add(name)
  return sum(1 + find_contained_by(bag, visited) if bag not in visited else 0 for bag in bags[name].containedBy)

print(find_contained_by('shiny gold', set())) # part 1

def find_contains(name: str) -> int:
  return sum(v + v * find_contains(k) for k, v in bags[name].contains.items())

print(find_contains('shiny gold')) # part 2