import re

def open_file():
    with open('Day 4.txt') as f:
        return list(map(str.strip, f.readlines()))


def sort_content(content):
    pattern = re.compile('')
    for line in content: