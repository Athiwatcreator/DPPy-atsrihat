number_text = input("Give me a number: ")

try:
    number = float(number_text)
except ValueError:
    print("That is not a valid number.")
else:
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")