def open_file():
    with open('Day 5.txt', 'r') as f:
        return list(f.readline().strip())


def filter_polymers(content):
    i = 0
    while i < len(content)-1:
        c1 = content[i]
        c2 = content[i+1]
        if str.upper(c1) == str.upper(c2) and \
                ((str.isupper(c1) and str.islower(c2))
                    or
                    (str.islower(c1) and str.isupper(c2))):
            del content[i:i+2]
            i -= (2 if i > 0 else 1)
        i += 1
    return content


line = open_file()
print(len(line))
print(len(filter_polymers(line)))
