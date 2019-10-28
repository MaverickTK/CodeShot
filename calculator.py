#A simple calculator

#commaSeperated
#spaceSeperated

#newLine : loop
def get_input():
    """to get input from user"""
    numbers = []
    numbers_string = input("Enter comma separated integer value - ")
    for num in numbers_string.split(','):
        numbers.append(int(num))
    print(numbers)
    return numbers

def add():
    """to add number of numbers"""
    # numbers = []
    # Approach One
    # while True:
    #     num  = int(input("Enter the numbers, Input 999999999 to exit"))
    #     if(num == 999999999):
    #         break
    #     else:
    #         numbers.append(num)

    # Approach Two
    # numbers_string = input("Enter comma separated integer value - ")
    #'1,2,3,4,5,6,7,8,9,10'
    numbers = get_input()
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
    return sum

def sub():
    """to input two numbers from user and evaluate their difference"""
    n1=int(input("enter a no.-"))
    n2=int(input("enter a no.-"))
    diff=0
    diff=n1-n2
    print(diff)
    return diff

def mul():
    """to take numbers from users and multiply them"""
    numbers_string = input("Enter comma separated integer value - ")
    #'1,2,3,4,5,6,7,8,9,10'
    numbers = get_input()
    prod = 1
    for num in numbers:
        prod = prod * num
    print(prod)
    return prod

def div():
    """to take two numbers and divide them""" 
    n1=int(input("enter a no.-"))
    n2=int(input("enter a no.-"))
    div=0
    div=n1/n2
    print(div)
    return div
def square():
    """to take an no and then to find square"""
    n=int(input("enter a no-"))
    print(n*n)
    return n*n


def show_menu():
    '''
    Shows the list of available operations
    :return: None
    '''
    print('\n\n','*'*70)
    print("Choose from the following")
    print("1. Add")
    print("2. Subtract two numbers")
    print("3. Multiply")
    print("4. Divide")
    print("5. square")
    print("6. Exit the program")
    option = input("Enter your choice of operation to be performed - ")
    print('\n')
    if option == str(6):
        print("exiting the function")
        exit(0)
    elif option ==str(5):
        square()
    elif option == str(4):
        div()
    elif option == str(3):
        mul()
    elif option == str(2):
        sub()
    elif option == str(1):
        add()
        # nums = input('user')
        # add(*args)

# option = input("Enter your choice of operation to be performed")
#

while True:
    show_menu()
    # option = input("Enter your choice of operation to be performed")
    # if option == str(6):
    #     break
    # elif option ==str(5):
    #     square()
    # elif option == str(4):
    #     div()
    # elif option == str(3):
    #     mul()
    # elif option == str(2):
    #     sub()
    # elif option == str(1):
    #     add()
