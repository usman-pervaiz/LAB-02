def f(num):
    """This function converts decimal number
    to octal and prints it"""
    if num > 7:
        f(num // 8)
    print(num % 8, end='')
# decimal number
number = int(input("Enter any decimal number: "))
f(number)


