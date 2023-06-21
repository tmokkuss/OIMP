import re

COMMA = ", "
ENTER = "\n"
TOP = 10


def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
        return content


def write_data(out_file_name, file_name):
    data = add_enters(file_name)
    with open(out_file_name, "w") as file:
        file.writelines(data)


def find_count_symbols(data):
    pattern = r'[A-Za-z]'
    content = data
    symbols = re.findall(pattern=pattern, string=content)
    visited = set()
    duplicates_set = {}
    key = [x for x in symbols if x in visited or (visited.add(x) or False)]

    for index, i in enumerate(key):
        duplicates_set[key[index]] = 1

    for x in key:
        if x in duplicates_set:
            duplicates_set[x] += 1
        else:
            duplicates_set[x] = 1
    return sorted(duplicates_set.items(), key=lambda x: x[-1], reverse=True)


def add_enters(data):
    content = data
    row = []
    for i in content:
        for index, x in enumerate(i):
            if type(x) == int:
                number = str(x)
                row.append(COMMA + number + ENTER)
            else:
                row.append(x)
    return row[:(TOP*5+3)]


if __name__ == '__main__':
    content = read_data("input.txt")
    data = find_count_symbols(content)
    data_for_write = add_enters(data)
    write_data("output.txt", data_for_write)