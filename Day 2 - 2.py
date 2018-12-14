from itertools import combinations


def open_file():
    with open('Day 2.txt', 'r') as f:
        return list(map(str.strip, f.readlines()))


def find_strings(lines):
    comb = combinations(lines, 2)
    for x, y in comb:
        diff = 0
        letters = []
        for a, b in zip(x, y):
            if a != b:
                diff += 1
            else:
                letters.append(a)
            if diff > 1:
                break
        else:
            return ''.join(letters)


content = open_file()
print(find_strings(content))
