from itertools import permutations
import math
import re
from typing import Dict, List, Set, Tuple

class Rule:
  def __init__(self, input: List[Tuple[str, str, str, str, str]]):
    self.name: str = input[0][0]
    self.ranges: List[Tuple[int, int]] = [(int(input[0][1]), int(input[0][2])), (int(input[0][3]), int(input[0][4]))]
    self.col: List[int] = []

  def match(self, num: int) -> bool:
    return any(num >= r[0] and num <= r[1] for r in self.ranges)

  def test(self, tickets: List[List[int]]):
    for col in range(len(tickets[0])):
      if all(self.match(t[col]) for t in tickets):
        self.col.append(col)

def parse(data: List[str]) -> Tuple[List[Rule], List[int], List[List[int]]]:
  i = 0
  rules: List[Rule] = []
  mine: List[int] = []
  nearby: List[List[int]] = []
  while len(data[i]) > 0:
    rules.append(Rule(re.findall(r"([^:]+): (\d+)-(\d+) or (\d+)-(\d+)", data[i])))
    i += 1
  i += 2
  mine = [int(x) for x in data[i].split(',')]
  i += 3
  while i < len(data):
    nearby.append([int(x) for x in data[i].split(',')])
    i += 1
  return (rules, mine, nearby)

def process(nearby: List[List[int]], rules: List[Rule]) -> Tuple[int, List[List[int]]]:
  filtered = []
  errorrate = 0
  for t in nearby:
    good = True
    for i in t:
      if not any(r.match(i) for r in rules):
        errorrate += i
        good = False
    if good:
      filtered.append(t)
  return (errorrate, filtered)

def order(rules: List[Rule], tickets: List[List[int]]) -> List[Rule]:
  [r.test(tickets) for r in rules]
  rules.sort(key=lambda x: len(x.col))
  ordered = {}
  for i in range(len(rules)):
    ordered[rules[i].col[0]] = rules[i]
    for j in range(i+1, len(rules)):
      rules[j].col.remove(rules[i].col[0])
  return [ordered[i] for i in range(20)]

def compute(rules: List[Rule], mine: List[int]) -> int:
  return math.prod(mine[i] for i, r in enumerate(rules) if r.name.startswith('departure'))

if __name__ == "__main__":
  with open('day16input') as f:
    data = [s.strip('\n') for s in f.readlines()]
  rules, mine, nearby = parse(data)
  errorrate, filtered = process(nearby, rules)
  print(errorrate) # part 1
  rules = order(rules, [mine] + filtered)
  print(compute(rules, mine)) # part 2