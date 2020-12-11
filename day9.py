from typing import List

def find_weakness(data: List[int]) -> int:
  begin, end = 0, 25
  for i in range(25, len(data)):
    found = False
    for j in data[begin:end]:
      if data[i] - j in data[begin:end]:
        found = True
        break
    if not found:
      return data[i]
    begin += 1
    end += 1
  return -1

def find_chain(data: List[int], target) -> int:
  for i in range(len(data)):
    sum = 0
    j = i
    while sum < target:
      sum += data[j]
      j += 1
    if sum == target:
      return min(data[i:j-1]) + max(data[i:j-1])
  return -1


if __name__ == "__main__":
  data = []
  with open('day9input') as f:
    data = [int(s) for s in f.readlines()]
  target = find_weakness(data)
  print(target) # part 1
  print(find_chain(data, target)) # part 2