def add(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation_dict = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "%": divide
}
run = True
a = int(input("Enter the first number: "))
while run:
    operator = input("What will be the calculation? (+ or - or * or /) ")
    b = int(input("Enter the next number: "))
    result = operation_dict[operator](a, b)

    print(f"The result is {result}.")
    answer = input(f"Would you like to procced with the result {result}? y or n ")
    if answer == "n":
        run = False
    else:
        a = result

