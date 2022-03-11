from  Clinic import *
from Doctor import *
from Holidays import *
from datetime import date


def main():

    """
    main method will be called if bookingsystem.py is called from the command line
    This is because of the following lines at the end of files
    if __name__ == '__main__':
        main()

    if instead bookingsystem.py is imported nothing will happen, as main will not be running
    because __name__ != '__main__'

    """
    # First create some holidays - check https://docs.python.org/3/library/datetime.html to
    # get and overview of how date datetime.date functions.
    d1: date = date.fromisoformat('2022-04-07')
    d2: date = date.fromisoformat('2022-04-08')
    d3: date = date.fromisoformat('2022-04-08')
    d4: date = date.fromisoformat('2022-04-09')

    # now create an empty list of 'doctor holidays' and add a some days to the list
    doctor1_holidays = Holidays()
    doctor1_holidays.add_holiday(d1)
    doctor1_holidays.add_holiday(d2)
    doctor1_holidays.add_holiday(d4)

    # now create a doctor
    doctor1: Doctor = Doctor("A.S. Pirin",doctor1_holidays)

    # print doctor1's holidays
    print(f"{doctor1.name}'s holidays:")
    print(doctor1.list_holidays)

    # and another list of doctor-holidays and another doctor

    doctor2_holidays = Holidays()
    doctor2_holidays.add_holiday(d1)

    doctor2: Doctor = Doctor("P.A. Nodil", doctor2_holidays)

    # create a list of holidays for the a clinic

    clinic1_holidays = Holidays()
    clinic1_holidays.add_holiday(d1)
    clinic1_holidays.add_holiday(d2)
    clinic1_holidays.remove_holiday(d3) # what happens here? can you explain
    clinic1_holidays.add_holiday(d4)

    # create a list of doctors for the clinic
    list_doctors = [doctor1,doctor2]

    # create a clinic

    clinic1: Clinic = Clinic("Nørrebrolægerne" , "Nørrebrovej 27, 2100 Kbh N", clinic1_holidays, list_doctors )

    # print the list of holidays for the clinic:

    print(f"{clinic1.name}'s holidays:")
    print(clinic1.list_holidays)

    # Emulate some booking attempts and then ask for a booking date
    # I just check for the availability of a single doctor on a single clinic
    # We could also have iterated over alle doctors in the clinic and checked for their availability
    # The description of the task is a bit ambiguous.
    # Feel free to do make your own interpretation

    print("-"*30)
    print("Attempting bookings")
    print("-"*30)

    booking_date: date = date.fromisoformat('2022-04-07')
    print(f"Attempt: Booking {doctor1.name} on " + str(booking_date))
    print(doctor1.check_available(clinic1,booking_date))

    booking_date: date = date.fromisoformat('2022-04-08')
    print(f"Attempt: Booking {doctor1.name} on " + str(booking_date))
    print(doctor1.check_available(clinic1,booking_date))

    booking_date: date = date.fromisoformat('2022-04-07')
    print(f"Attempt: Booking {doctor1.name} on " + str(booking_date))
    print(doctor1.check_available(clinic1, booking_date))

    # Now ask the user for a booking date and see if it can be passed in iso-format
    # in task 2 and 3 we will try with some other formats

    print("-" * 30)
    print("Make your own bookings")
    print("-" * 30)

    while True:
        try:
            booking_date_input = input(f"Input a new booking date for {doctor1.name} in format YYYY-MM-DD or 'q/Q' for quit: ")
            if str.upper(booking_date_input) == "Q":
                break
            else:
                booking_date = date.fromisoformat(booking_date_input)
                # Do minimal check on the date - is it in the future?:
                if booking_date > date.today():
                    print(f"Attempt: Booking {doctor1.name} on " + str(booking_date))
                    print(doctor1.check_available(clinic1, booking_date))
                else:
                    print("You need to book a future date - try again")
        except:
            print(" not a valid booking date, try again")


if __name__ == '__main__':
    # We end here, if we run the python file from the command line - not if we include it
    # We just want to run the main method..
    # If we had made some classes, methods and functions that could be useful in other python projects
    # then the file could be imported without the main() method being run
    main()
