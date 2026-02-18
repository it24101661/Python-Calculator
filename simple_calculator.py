
#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return
    elif choice in ['+', '-', '*', '/', '^', '%']:
        # Get first number
        first = input("Enter first number: ")
        print(first)
        if '#' in first:
            print("Done. Terminating")
            exit()
        if '$' in first:
            return
        
        try:
            a = float(first)
        except:
            print("Not a valid number,please enter again")
            return
        
        # Get second number
        second = input("Enter second number: ")
        print(second)
        if '#' in second:
            print("Done. Terminating")
            exit()
        if '$' in second:
            return
        
        try:
            b = float(second)
        except:
            print("Not a valid number,please enter again")
            return
        
        # Perform operation
        if choice == '+':
            result = add(a, b)
            print(f"{a} + {b} = {result}")
        elif choice == '-':
            result = subtract(a, b)
            print(f"{a} - {b} = {result}")
        elif choice == '*':
            result = multiply(a, b)
            print(f"{a} * {b} = {result}")
        elif choice == '/':
            if b == 0:
                print("float division by zero")
                print(f"{a} / {b} = None")
            else:
                result = divide(a, b)
                print(f"{a} / {b} = {result}")
        elif choice == '^':
            result = power(a, b)
            print(f"{a} ^ {b} = {result}")
        elif choice == '%':
            if b == 0:
                print("float division by zero")
                print(f"{a} % {b} = None")
            else:
                result = remainder(a, b)
                print(f"{a} % {b} = {result}")
    else:
        print("Unrecognized operation")
    return

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()