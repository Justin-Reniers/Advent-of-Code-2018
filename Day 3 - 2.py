import re
import numpy as np


def open_file():
    with open('Day 3.txt', 'r') as f:
        return list(map(str.strip, f.readlines()))


def find_stuff(content):
    pattern = re.compile('(\d+)')
    ids = set()
    fabric = np.zeros((1000, 1000), dtype=int)
    for line in content:
        temp = list(map(int, (re.findall(pattern, line))))
        identity, x, y, dx, dy = temp
        ids.add(identity)
        for a in range(x, x + dx):
            for b in range(y, y + dy):
                el = fabric[a, b]
                if el != 0:
                    if el in ids:
                        ids.remove(el)
                    if identity in ids:
                        ids.remove(identity)
                fabric[a, b] = identity
    return ids


result = find_stuff(open_file())
print(result)
