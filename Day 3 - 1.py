import re
import numpy as np


def open_file():
    with open('Day 3.txt', 'r') as f:
        return list(map(str.strip, f.readlines()))


def find_stuff(content):
    pattern = re.compile('(\d+)')
    fabric = np.zeros((1000, 1000), dtype=int)
    for line in content:
        x1, x2, x3, x4, x5 = re.findall(pattern, line)


find_stuff(open_file())
