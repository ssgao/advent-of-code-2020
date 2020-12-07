import re
from typing import Dict

hclRegex = re.compile('#[0-9a-f]{6}')
passports = []
rules = {'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
         'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
         'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
         'hgt': lambda x: (x.endswith('cm') and x.strip('cm').isdigit() and int(x.strip('cm')) >= 150 and int(x.strip('cm')) <= 193) or \
                          (x.endswith('in') and x.strip('in').isdigit() and int(x.strip('in')) >= 59 and int(x.strip('in')) <= 76),
         'hcl': lambda x: bool(hclRegex.match(x)),
         'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
         'pid': lambda x: x.isdigit() and len(x) == 9}

with open('day4input') as f:
  current: Dict[str, str] = {}
  for line in f.readlines():
    if len(line.strip()) == 0:
      passports.append(current)
      current = {}
    else:
      current = current | dict(s.split(':') for s in line.strip().split(' '))
  if len(current) > 0:
    passports.append(current)

def check(p: dict) -> bool:
  return set(rules.keys()).issubset(p.keys()) and all(key == 'cid' or rules[key](value) for key, value in p.items())

print(sum(check(p) for p in passports))