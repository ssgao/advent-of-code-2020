import functools
from typing import Callable, List, Set

data: List[str] = []
with open('day6input') as f:
    data = [l.strip() for l in f.readlines()]


def get_answers(func: Callable[[Set[str], Set[str]], Set[str]]):
    answers: List[Set[str]] = []
    a: List[Set[str]] = []
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