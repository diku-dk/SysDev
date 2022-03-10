from  Clinic import *
from Doctor import *

list_holidays_clinic = ['2022-01-07', '2022-01-08']

list_holidays_doctor1 = ['2022-01-04', '2022-01-05' , '2022-01-11']
list_holidays_doctor2 = ['2022-01-10', '2022-01-11']

doctor1 = Doctor("A.S. Pirin", list_holidays_doctor1)
doctor2 = Doctor("P.A. Nodil", list_holidays_doctor2)

list_doctors = [doctor1,doctor2]

clinic = Clinic("Nørrebrolægerne","Nørrebrovej 27, 2100 Kbh N", list_holidays_clinic, list_doctors )

#print(clinic)

#print(f"Feriedage for ", doctor1.name, " ", doctor1.list_holidays)

booking_date = input("Input a booking date in the format YYYY-MM-DD: ")
print("Booking date:", booking_date)

# Check if booking date in in clinic's list of holidays

if booking_date in clinic.list_holidays:
    print("Sorry we are on holiday")
    exit()

available = False

for doctor in clinic.list_doctors:
    if not (booking_date in doctor.list_holidays):
        available = True
        break

if available:
    print(" Booking is valid")
else:
    print(" Sorry no doctors available")

