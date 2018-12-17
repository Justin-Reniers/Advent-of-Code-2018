import string
import copy

def open_file():
    with open('Day 5.txt', 'r') as f:
        return list(f.readline().strip())


def filter_polymers(content):
    values = []
    for c in string.ascii_lowercase:
        i = 0
        j = 0
        temp = copy.deepcopy(content)
        while j < len(temp):
            if str.lower(temp[j]) == c:
                del temp[j]
                j -= 1
            j += 1
        while i < len(temp)-1:
            c1 = temp[i]
            c2 = temp[i+1]
            if str.upper(c1) == str.upper(c2) and \
                    ((str.isupper(c1) and str.islower(c2))
                        or
                        (str.islower(c1) and str.isupper(c2))):
                del temp[i:i+2]
                i -= (2 if i > 0 else 1)
            i += 1
        values.append(len(temp))
    return min(values)


# line = list('dabAcCaCBAcCcaDA')
line = open_file()
print(filter_polymers(line))
