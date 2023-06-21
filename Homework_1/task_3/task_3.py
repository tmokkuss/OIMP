import re

ENTER = '\n'
SPACE = ' '
ROW_LENGTH = 20


def read_data(file_name):
    with open(file_name) as file:
        content = file.read()
        return content


def write_data(out_file_name, data):
    data = data
    with open(out_file_name, "w") as file:
        file.writelines(data)


def format_text(content):
    words = content.split()
    lines = []
    row = ""
    for word in words:
        if len(row + SPACE + word) <= ROW_LENGTH:
            row = row + SPACE + word
        else:
            lines.append(row.strip())
            row = word
    lines.append(row.strip())
    formatted_text = ENTER.join(lines)
    return formatted_text


if __name__ == '__main__':
    content = read_data("input.txt")
    data = format_text(content)
    write_data("output.txt", data)