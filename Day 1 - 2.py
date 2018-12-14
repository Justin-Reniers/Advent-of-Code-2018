def open_file():
    with open('Day 1.txt', 'r') as f:
        lines = f.readlines()
        int_list = [int(i) for i in lines]
        return int_list


def find_duplicate(int_list):
    summation = 0
    frequencies = {0}
    while True:
        for x in int_list:
            summation += x
            if summation in frequencies:
                return summation
            frequencies.add(summation)


ints = open_file()
result = find_duplicate(ints)
print(result)
