import re


def open_file():
    with open('Day 4.txt') as f:
        return list(map(str.strip, f.readlines()))


def sort_content(content):
    p1 = re.compile('')
    p2 = re.compile('([0-9]+)-([0-9]+)-([0-9]+)\s([0-9]+):([0-9]+)')
    for line in content:
        pass