# Week 1 exercise 2.
# Make a program that calculates the cost of an admission in a private hospital
# during X days length at the price of Y per day
# We have tried to add a little input validation...


def print_price(value: float):
    print(f'The total prise is: {value:8.2f}')


if __name__ == '__main__':
    while True:
        days_input = input("Number of days: ")
        try:
            days_int = int(days_input)
        except:
            print("days must be integer")
            continue

        dayPrice_input = input("Price pr day: ")

        try:
            dayPrice_float = float(dayPrice_input)
        except:
            print("day price must be a floating point number.")
            continue

        price: float = dayPrice_float * days_int
        print_price(price)
        exitInput = input("press q to exit or any other key for new calculation: ")
        if exitInput == "q":
            exit(0)
