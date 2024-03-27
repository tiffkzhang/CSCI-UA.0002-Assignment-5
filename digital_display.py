
def horizontal_line(char: str):
    print(char * 5)

def vertical_line(char: str, shift: int, height: int):
    for i in range(height):
        print(' ' * shift, char, sep='')

def two_vertical_lines(char: str, height: int):
    for i in range(height):
        print(char,'   ', char, sep='')

def number_0(char):
    horizontal_line(char)
    two_vertical_lines(char, 3)
    horizontal_line(char)

def number_1(char):
    vertical_line(char, 4, 5)

def number_2(char):
    horizontal_line(char)
    vertical_line(char, 4, 1)
    horizontal_line(char)
    vertical_line(char, 0, 1)
    horizontal_line(char)

def number_3(char):
    horizontal_line(char)
    vertical_line(char, 4, 1)
    horizontal_line(char)
    vertical_line(char, 4, 1)
    horizontal_line(char)

def number_4(char):
    two_vertical_lines(char, 2)
    horizontal_line(char)
    vertical_line(char, 4, 2)

def number_5(char):
    horizontal_line(char)
    vertical_line(char, 0, 1)
    horizontal_line(char)
    vertical_line(char, 4, 1)
    horizontal_line(char)

def number_6(char):
    horizontal_line(char)
    vertical_line(char, 0, 1)
    horizontal_line(char)
    two_vertical_lines(char, 1)
    horizontal_line(char)

def number_7(char):
    horizontal_line(char)
    two_vertical_lines(char, 2)
    vertical_line(char, 4, 2)

def number_8(char):
    horizontal_line(char)
    two_vertical_lines(char, 1)
    horizontal_line(char)
    two_vertical_lines(char, 1)
    horizontal_line(char)

def number_9(char):
    horizontal_line(char)
    two_vertical_lines(char, 1)
    horizontal_line(char)
    vertical_line(char, 4, 2)

def plus(char):
    vertical_line(char, 2, 2)
    horizontal_line(char)
    vertical_line(char, 2, 2)

def minus(char):
    horizontal_line(char)


def check_answer(num_1: int, num_2: int, answer: int, operater: str):
    if operater == '+':
        return(num_1 + num_2 == answer)
    else:
        return(num_1 - num_2 == answer)