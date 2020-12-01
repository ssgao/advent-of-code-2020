data = []
with open('day1input') as f:
  data = [int(i) for i in f.readlines()]

# Part 1
knownNumbers = set()
for d in data:
  if 2020-d in knownNumbers:
    print(d * (2020-d))
    break
  else:
    knownNumbers.add(d)

# Part 2
numMap = {}
for d in data:
  if d >= 2019:
    continue
  max = 2019-d
  for f in data:
    if f >= max-1:
      continue
    numMap[2020-d-f] = (d, f)

for d in data:
  if d in numMap:
    f, g = numMap[d]
    print(d * f * g)
    break