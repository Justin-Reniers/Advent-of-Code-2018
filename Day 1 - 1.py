def open_file():
    with open('Day 1.txt', 'r') as f:
        lines = f.readlines()
        int_list = [int(i) for i in lines]
        return int_list


numbers = open_file()
print(sum(numbers))
