import math
import os

def mult(a,b) -> int:
    return math.floor(a * b)


def add(a, b) -> int:
    return math.floor(b + a)


def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
