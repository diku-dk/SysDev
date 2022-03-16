from Employee import Employee

def main():
    emp1 = Employee("Anders", "Andersen", "100181-101", "+4512121212", "anders.andersen@company.com")
    print(emp1)
    print("changing phone number")
    emp1.set_phone("+4533333333")
    print(emp1)
    emp2 = Employee("Bente", "Bentsen", "020282-0202", "+4566666666", "bente.bentsen@company.com")
    print(emp2)
    print("Marrying Anders and Bente")
    emp2.set_last_name("Andersen")
    emp2.set_email("bente.andersen@company.com")
    print(emp2)

    print(f"The cpr-number of {emp2.get_first_name()} {emp2.get_last_name()} is {emp2.get_cpr_number()}")
    print(f"{emp2.get_first_name()} is {emp2.get_age()} years old")


if __name__ == '__main__':
    main()
