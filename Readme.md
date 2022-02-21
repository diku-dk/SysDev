# Week2_1 programming exercise - proposed solution

`main.py` has been split into two files `main.py`and `validator.py`.

The validator module is used to validate the user input.

Two test module have been created: `test_main.py` and `test_validator.py`

They contain tests for functions defined in `main.py` and in `validator.py`.

Please note the implementation of cpr validation only allows for real valid cpr-numbers.
So if you want to run those tests, then remove the comments and try with your own
cpr number. I did try to run with the official medcom test cpr numbers found here:  
https://www.medcom.dk/opslag/koder-tabeller-ydere/tabeller/nationale-test-cpr-numre , 
but they didn't validate.
I didn't have the time to check if it was the mod 11 check they didn't pass.
(Feel free to rewrite the code to bypass that check and see if it works then...)
