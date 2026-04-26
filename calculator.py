def add(a, b):
    print(f"{a} + {b}= ", a + b)


def sub(a, b):
    print(a - b)


def mul(a, b):
    print(a * b)


def div(a, b):
    print(a / b)


while True:
    user_input1 = int(input("Enter Number:"))
    user_input2 = int(input("Enter Number: "))
    print(f"1st Number= {user_input1} 2nd Number = {user_input2}")

    print("\n1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Division")

    operation = int(input("Choose Operation: "))

    if operation == 1:
        add(user_input1, user_input2)
    elif operation == 2:
        sub(user_input1, user_input2)
    elif operation == 3:
        mul(user_input1, user_input2)
    elif operation == 4:
        div(user_input1, user_input2)
    else:
        print("Enter a valid number")
