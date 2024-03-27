import digital_display
import random

problems = int(input('How many problems would you like to attempt? '))

while problems <= 0:
    print('Please enter a positive number.')
    problems = int(input('How many problems would you like to attempt? '))

character = input('\nWhat character would you like to print with? ')

while len(character) > 1:
    print('Please enter a single character.')
    character = input('What character would you like to print with? ')

print('\nHere we go!\n')

def print_num(num: int): # This prints the digital number
    if num == 0:
        digital_display.number_0(character)
    elif num == 1:
        digital_display.number_1(character)
    elif num == 2:
        digital_display.number_2(character)
    elif num == 3:
        digital_display.number_3(character)
    elif num == 4:
        digital_display.number_4(character)
    elif num == 5:
        digital_display.number_5(character)
    elif num == 6:
        digital_display.number_6(character)
    elif num == 7:
        digital_display.number_7(character)
    elif num == 8:
        digital_display.number_8(character)
    elif num == 9:
        digital_display.number_9(character)

def print_op(op: str): # This prints the digital operator
    if op == '+':
        digital_display.plus(character)
    else:
        digital_display.minus(character)

def main():
   
    correct = 0

    for i in range(problems):
        print('What is . . .\n')

        num_1 = random.randint(0,9) # Generates a random number 0-9
        num_2 = random.randint(0,9)

        operator = random.randint(0,1) # Generates a random operator
        if operator == 0:
            operator = '+'
        else:
            operator = '-'
        
        print_num(num_1) # Prints digital display
        print()
        print_op(operator)
        print()
        print_num(num_2)
        print()
        
        answer = int(input('= ')) # User input answer
        
        if digital_display.check_answer(num_1, num_2, answer, operator):
            correct += 1
            print('\nCorrect.\n')
            
        else:
            print('\nIncorrect.\n')
    
    print('You got', correct, 'out of', problems, 'correct.')

main()
    

    

    
    









