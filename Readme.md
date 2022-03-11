# Week 4_1 Exercise proposed solution

In order to solve the task three classes `Clinic`, `Doctor` and `Holidays` have been made.
(we solved it differently in the class at KU, but I have chosen to create this solution so 
that you have more info on how can be worked on classes)

`Holidays.py` contains the class `Holidays` which hold a list of dates to which holidays can be added and removed through methods. 
It also holds a method that returns `True` if a given date is in the list.

`Doctor.py` contains the class `Doctor` which holds a name and a list of holidays (we use an object of type Holiday to hold the list)

`Clinic.py` contains the class `Clinic` which hold its own list of holidays and a list of Doctors.

`bookingsystem.py` is the main executable. The comments in the code should make it self-explanatory.


The result of running bookingsystem.py should be something like:

```
A.S. Pirin's holidays:
Number of holidays: 3 
The holidays are 
2022-04-07, 2022-04-08, 2022-04-09
Nørrebrolægerne's holidays:
Number of holidays: 2 
The holidays are 
2022-04-07, 2022-04-09
------------------------------
Attempting bookings
------------------------------
Attempt: Booking A.S. Pirin on 2022-04-07
The clinic is closed on 2022-04-07 
Attempt: Booking A.S. Pirin on 2022-04-08
A.S. Pirin is on holiday on 2022-04-08
Attempt: Booking A.S. Pirin on 2022-04-07
The clinic is closed on 2022-04-07 
------------------------------
Make your own bookings
------------------------------
Input a new booking date for A.S. Pirin in format YYYY-MM-DD or 'q/Q' for quit: j341h4321
 not a valid booking date, try again
Input a new booking date for A.S. Pirin in format YYYY-MM-DD or 'q/Q' for quit: 2011-10-01
You need to book a future date - try again
Input a new booking date for A.S. Pirin in format YYYY-MM-DD or 'q/Q' for quit: 2022-04-08
Attempt: Booking A.S. Pirin on 2022-04-08
A.S. Pirin is on holiday on 2022-04-08
Input a new booking date for A.S. Pirin in format YYYY-MM-DD or 'q/Q' for quit: 2022-08-20
Attempt: Booking A.S. Pirin on 2022-08-20
A.S. Pirin is available on 2022-08-20
Input a new booking date for A.S. Pirin in format YYYY-MM-DD or 'q/Q' for quit: q

```

