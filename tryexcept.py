try:
    answer = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)  # Prints the actual error message, or use print("err") for literal text
except ValueError:
    print("Invalid input")