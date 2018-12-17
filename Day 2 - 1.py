from collections import Counter


def open_file():
    with open('Day 2.txt', 'r') as f:
        return f.readlines()


def checksum(lines):
    twice = 0
    thrice = 0
    for line in lines:
        list_filter = list(filter(lambda x: x >= 2, Counter(line).values()))
        if 2 in list_filter:
            twice += 1
        if 3 in list_filter:
            thrice += 1
    return twice*thrice


content = open_file()
result = checksum(content)
print(result)
