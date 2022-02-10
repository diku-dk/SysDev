# Exercise 5

Modify the program to perform minimal error checking: 
are strings only composed of non-number characters with a maximum length. 
CPR numbers and addresses will accept only formats valid in Denmark.
 


Modify the program you created in task 4 to perform minimal error checking.

Ensure that:

- A name can only consist of letters, not numbers.  
- A name is at least a first- and last name.  
- A CPR follows the format ddmmyy-XXXX.  

If the input patient data does not live up to the requirements, notify the user by printing a message.

If the data fulfils the requirements, print out the patient data, age and assigned gender as in task 4.
Consider using methods to perform your validation.

Bonus requirement: Check that the CPR number is valid with Mod11.  
https://da.wikipedia.org/wiki/Modulus_11  
https://da.wikipedia.org/wiki/CPR-nummer#Kontrolciffer_(det_gamle_CPR-nummer)

# Solution:

note: This is one way to do this. The exercise is very loose wrt. requirements and the learning goals are:

Get acquainted with Python
Realise that parsing data from a user is a massive endeavour
If any of the code is confusing, please ask Jakob or Leif to explain it in the exercise classes.

We have modified the solution from exercise 4 to use ```stdnum.dk.cpr``` which have cpr number handling.
(in the solution for exercise 4 we copied some functions from ```stdnum.dk.cpr``` ).

Please be aware that the variable to store the cpr number is now called ```cpr_number```
(otherwise it would class with the cpr library functions)

We first define functions that we will need (and that we don't get from stdnum.dk.cpr):  
The three functions ```get_name, get_cpr, get_address``` take care of inputs.   
The two functions ```gender``` and ```age``` will calculate the gender and the age.

```get_name``` will need to verify the length of the name and the number of "sub" names".  
It will also need to check if the name only contains letters 
(we don't handle special names like o'Harry)

```get_cpr``` needs to validate the cpr-number - here we have used the  ```stdnum.dk.cpr``` library (why re-invent the wheel?)

```get_address``` performs similar checks.

Several enhancements can be done and is up to the student!  
The code hasn't been thoroughly tested!

If you don't want to type in real cpr-numbers while testing, then you can
either find and disable the check in the code or you can search for "valid" test cpr-numbers and try with those.

Utf-8 inputs (like Danish æ,ø,å) can be a challenge. 
You might need to look into decode/encode methods (try google python input utf-8).
And you will most likely need it in your future project(s)



