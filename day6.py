import functools
from typing import Callable

data = []
with open('day6input') as f:
    data = [l.strip() for l in f.readlines()]


def get_answers(func: Callable[[set], set]):
    answers = []
    a = []
    for l in data:
        if len(l) == 0:
            answers.append(functools.reduce(func, a))
            a = []
        else:
            a.append(set(l))
    answers.append(functools.reduce(func, a))
    return answers


print(sum(len(x) for x in get_answers(lambda a, b: a | b))) # part 1
print(sum(len(x) for x in get_answers(lambda a, b: a & b))) # part 2