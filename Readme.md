Suggestion solution to Exercise 5_1:

Task:
```
An Employee class
Create a class for managing employees ie. the Employee class, with the following private attributes:

- first name
- last name
- CPR number (bonus: how do you ensure that the CPR is written correctly?)
- telephone number (bonus: how do you ensure that this is a valid telephone number?)
- E-mail (bonus: how do you ensure that this is a valid email address?)

Add the following public get- and set-methods: 

- getFirstname()
- setFirstName(newName)
- getLastName()
- setLastName()
- getCPR()
- setCPR(newCPR)
- getPhoneNumber()
- setPhoneNumber(newPhoneNumber)
- getEmail()
- setEmail(newEmail)
- getAge() - (this attribute is calculated from the CPR number, so there are no setter for this, and no private attribute)
```

The `Employee` class is in `Employee.py`.
Note the user of double underscores in front of the attributes, which make the attributes private.
Hence, the following code will throw an exception error

```python
# WRONG - will not work!
from Employee import Employee
emp1=Employee("Test","Testesen", '111111-1111', '+1111111111', "test.testensen@test.com")
print(emp1.__first_name)
```

The right way to print the first name of the `emp1` object would be by using the getter:

```python
from Employee import Employee
emp1=Employee("Test","Testesen", '111111-1111', '+1111111111', "test.testensen@test.com")
print(emp1.get_first_name())
```

I have also made use of the cpr module from stdnum.dk in order to calculate the age
from the cpr number.

Note that the Employee class can be further enhanced by adding validation tests through the
`Validator` class from earlier exercises on the constructor and the setters. This could be 
implemented via try/except statements where a faulty parameter could throw an exception.



