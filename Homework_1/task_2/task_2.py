ENTER = '\n'
PREFIX = 'KP2.2-'
SEPARATOR = ' - '


def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
        return content


def write_data(out_file_name, data):
    data = data
    with open(out_file_name, "w") as file:
        file.writelines(data)


def sort_data(data):
    data_for_sort = data.splitlines()
    values_list = []
    for file_names in data_for_sort:
        value = file_names[file_names.index(PREFIX) + len(PREFIX):file_names.index(SEPARATOR)]
        values_list.append(float(value))
    values_and_rows = list(zip(values_list, data_for_sort))
    sorted_data = []
    for i in sorted(values_and_rows):
        sorted_data.append(str(i[1]) + ENTER)

    return sorted_data


if __name__ == '__main__':
    content = read_data("input.txt")
    data = sort_data(content)
    write_data("output.txt", data)