from typing import Dict, List, Set

class Bag:
  def __init__(self):
    self.contains: Dict[str, int] = {}
    self.containedBy: Set[str] = set()

def build_graph(data: List[str]) -> Dict[str, Bag]:
  bags: Dict[str, Bag] = {}
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
  return bags

def print_graph(bags: Dict[str, Bag]):
  print(*(f'{k}: {v.contains} & {v.containedBy}\n' for k, v in bags.items()))

def find_contained_by(name: str, visited: Set[str], bags: Dict[str, Bag]) -> int:
  visited.add(name)
  return sum(1 + find_contained_by(bag, visited, bags) if bag not in visited else 0 for bag in bags[name].containedBy)

def find_contains(name: str, bags: Dict[str, Bag]) -> int:
  return sum(v + v * find_contains(k, bags) for k, v in bags[name].contains.items())

if __name__ == "__main__":
  data = []
  with open('day7input') as f:
    data = [s.strip('.\n').replace(' bags', '').replace(' bag', '') for s in f.readlines()]
  bags: Dict[str, Bag] = build_graph(data)
  print(find_contained_by('shiny gold', set(), bags)) # part 1
  print(find_contains('shiny gold', bags)) # part 2