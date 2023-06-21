import re


COMMA = ","
ENTER = "\n"


def read_data(file_name):
    with open(file_name) as file:
        content = file.read().splitlines()
        return content


def get_grade_and_name(data):
    data = data
    name = ''
    grade = ''
    list_of_students = []
    pattern_for_get_name = r'[0-9.:]'
    for i in data:
        name = re.sub(pattern_for_get_name, "", i).strip(" ")
        grade = i[-1]
        list_of_students.append(name + COMMA + grade + ENTER)

    return list_of_students


def alphabetical_sorting(data):
    content = data
    return sorted(content, key=lambda x: x.split(" ")[0].upper())


def write_data(out_file_name, data):
    data = data
    with open(out_file_name, "w") as file:
        file.writelines(data)


if __name__ == '__main__':
    content = read_data("data.txt")
    grade_and_name = get_grade_and_name(content)
    data = alphabetical_sorting(grade_and_name)
    write_data("output.csv", data=data)