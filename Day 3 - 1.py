import re
import numpy as np


def open_file():
    with open('Day 3.txt', 'r') as f:
        return list(map(str.strip, f.readlines()))


def find_stuff(content):
    pattern = re.compile('(\d+)')

    fabric = np.zeros((1000, 1000), dtype=int)
    for line in content:
        temp = list(map(int, (re.findall(pattern, line))))
        _, x, y, dx, dy = temp
        for a in range(x, x + dx):
            for b in range(y, y + dy):
                fabric[a, b] += 1
    return len(list(filter(lambda z: z > 1, np.asarray(fabric.ravel()))))


result = find_stuff(open_file())
print(result)
