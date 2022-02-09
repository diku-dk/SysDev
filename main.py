# Week1 Exercise 3:
# Create a program that tells a patient whether his/her
# blood percentage (Links to an external site.) requires attention.
# Man måler hæmoglobinniveauet ved at tage en blodprøve.
# Normalområdet for koncentrationen af hæmoglobin hos voksne:
#
# Male: 8.3-10.5 mmol/L
# Female: 7.3-9.5 mmol/L
#
# Notice that decimal(floating) numbers must be entered as "," (e.g 9,5)
# in the console if using danish locale
#
# E.g. try to enhance the code to ignore the case of the input!
# or to keep asking in a loop until the user types a special character

if __name__ == '__main__':

    bp: float

    bpMaleLowWaterMark: float = 8.3;
    bpMaleHighWaterMark: float = 10.5;
    bpFemaleLowWaterMark: float = 7.3;
    bpFemaleHighWaterMark:float = 9.5;

    print("Please enter your sex (M/F), and blod percentage in mmol/L")
    sex = input("Sex (M/F): ")
    while True:
        try:
            bp = float(input("Blood percentage in mmol/L: "))
            break
        except:
            print("must be a floating point number")

    if sex == 'M':
        if bp <= bpMaleLowWaterMark:
            print("Your blood percentage is too low\nPlease see a doctor")
        elif bpMaleLowWaterMark <= bp <= bpMaleHighWaterMark:
            print("Your blood percentage is fine")
        else:
            print("Your blood percentage is too high\nPlease see a doctor")
    elif sex == 'F':
        if bp <= bpFemaleLowWaterMark:
            print("Your blood percentage is too low\nPlease see a doctor")
        elif bpFemaleLowWaterMark <= bp <= bpFemaleHighWaterMark:
            print("Your blood percentage is fine")
        else:
            print("Your blood percentage is too high\nPlease see a doctor")
    else:
        print("Sex must be M (Male) or F (Female)")

    input("Press return to Exit:")
