# Week 2 Exercise 1

## Introduction

In this exercise we will take a look at test-driven development (TDD).
In TDD you specify the tests based on your requirements.
The tests are unit tests, that tests part of your code (functions, classes and methods etc). 
At first all your tests will fail, but as you progress with the implementation fewer and 
fewer errors will occur until your program finally will pass the test.

In Python the tests can be made by using the pytest test framework (other test frameworks exist as well).  
(You can read all about pytest here https://docs.pytest.org/ - or get some basic hints below)

You can write the tests yourself, or you could let someone else with a little Python 
programming knowledge do it.
(As you have already discussed in the conceptual exercises this can be beneficial 
as you - as a programmer - often can be biased and hence miss important aspects of the tests.)

You have actually already met pytest in your programming course.
Pytest was used in order to validate your hand-ins. The tests were implemented by your teacher or instructors.
You had passed your hand-in once all the tests were passed.

If we look at your second hand-in, your fist exercise was to create a function ```read_data```
that opens a file with data sets (two columns of floats) and return the values as a list of list of floats.

The second exercise was to write a function called ```calc_averages``` that takes a list of list of floats as 
input, and calculates the average value for each column by iterating over the rows.  
The function should return these two values.

The Python file with the unit tests that evaluated your code was called handin2_unit_test.py and the first lines of the code was:

```python
import os
import pytest

import handin2

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    pass
    
def teardown_module(module):
    '''Cleanup process'''
    pass

def test_python_ex1():
    '''Check read_data function'''
    global list_of_rows

    # Check that the function has a doc-string
    assert handin2.read_data.__doc__ !=  None

    # Call function
    list_of_rows = handin2.read_data('experimental_results.txt')

    # Check for number of lines
    assert len(list_of_rows) == 1000

    # Check that there are two values in last line
    assert len(list_of_rows[-1]) == 2
    
def test_python_ex2():
    '''Check calc_averages function'''

    # Check that the function has a doc-string
    assert handin2.calc_averages.__doc__ !=  None

    # Call function
    averages = handin2.calc_averages(list_of_rows)

    # Check that there are two return values
    assert len(averages) == 2

    # Check individual return values
    assert pytest.approx(averages[0], 1E-5) == 0.49505
    assert pytest.approx(averages[1], 1E-5) == 0.49895



```

The ```import pytest```statement enabled the pytest framework.
The ```import handin2``` statement imported the hand-in python file and hence gave acces to the 
functions that you had written.

The two functions
```python
def setup_module(module):
    """Cleanup process"""
    pass
```    
and
```python 
def teardown_module(module):
    """Cleanup process"""
    pass
```
will not be used for now, but we will touch it a later state of the course.
(It could e.g. be used to overwrite the input function - so that you can emulate user inputs from the
console)

The next function defines the first of the unit tests:

```python
def test_python_ex1():
    """Check read_data function"""
    global list_of_rows

    # Check that the function has a doc-string
    assert handin2.read_data.__doc__ !=  None

    # Call function
    list_of_rows = handin2.read_data('experimental_results.txt')

    # Check for number of lines
    assert len(list_of_rows) == 1000

    # Check that there are two values in last line
    assert len(list_of_rows[-1]) == 2
```

First a global variable `list_of_rows` is defined as it will be used during the remainder of the tests

The next code line is the first actual test. 
```python
# Check that the function has a doc-string
assert handin2.read_data.__doc__ !=  None
```

The assert statement is normally used in python to debug code - it writes a useful information to the user if the
condition is not met. With pytest you also use the assert statements in order to test your code.
We assert that the docstring is existing (!= None) and hence we test that you have written some
(prehaps) useful comments about what your function does

The person who gave you the data set (and wrote the test) knew that it contained 1000 lines and that the last line contained two values, 
so the next three  lines of the test is to read the file using your provided function and then assert that the length of the list
provided by your ```read_data``` function is 1000 and assert that the last line found has indeed
two values.

The next unit test is defined in

```python
def test_python_ex2():
    """Check calc_averages function"""

    # Check that the function has a doc-string
    assert handin2.calc_averages.__doc__ !=  None

    # Call function
    averages = handin2.calc_averages(list_of_rows)

    # Check that there are two return values
    assert len(averages) == 2

    # Check individual return values
    assert pytest.approx(averages[0], 1E-5) == 0.49505
    assert pytest.approx(averages[1], 1E-5) == 0.49895
```

This test tests the `calc_averages` function. We use the pytest.approx function in order to
test the return values with some level of tolerance - see https://docs.pytest.org/en/7.0.x/reference/reference.html?highlight=approx#pytest.approx


## Exercise:

*Write unit tests for your solution to last week's exercise.*

Follow this guide to create your tests https://www.jetbrains.com/help/pycharm/pytest.html

If you didn't make your own solution or didn't implement functions then use the solution provided here:
https://github.com/jakob-andersen/SystemsDevelopment2022/tree/Week1_5 as your starting point and write tests for the functions
`gender()` and `age()`.

In order to test the functions `get_name`, `get_address` and `get_cpr` a little more work needs to be
done: 

We will need to temporarily replace the build-in input function with our own, so that the automated
tests don't need to wait for user-input. This is done by using the `monkeypatch` functions in pytest.
See https://docs.pytest.org/en/7.0.x/how-to/monkeypatch.html ,
https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call and the answer by AlexG here
https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call/55033710#55033710


In our case we will need to do something like the following in order to test the `get_name` function
```python


import mock
import main

def test_get_name():
    with mock.patch.object(__builtins__, 'input', lambda: 'Jakob Andersen'):
        assert main.get_name() == 'Jakob Andersen'
    with mock.patch.object(__builtins__, 'input', lambda: 'Ja34 An65ersen'):
        assert main.get_name() != 'Ja34 An65ersen'
    

```

However, we will quickly realize that we will run into problems with the above approach, as the second `assert` line will
never end (as the current implementation of `get_name` will keep asking for a valid name).

A solution will be to rewrite the `get_*` functions to make them more testable and extract the code that do
the actual validation in separate functions called from the while loops.

e.g.

```python

def validate_cpr(input_cpr: str) -> bool:
    """
    Function that takes as input the cpr-number as a string
    and returns a bool telling whether it is valid or not
    """
    # check if the format is valid - use a function from "stdnum.dk.cpr"
    # note that the function requires the '-' to be removed first
    input_cpr = cpr.compact(input_cpr)
    valid = cpr.is_valid(input_cpr)
    # check if the cpr checksum is valid (modulus 11 rule) -
    # see the calculation done in https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/dk/cpr.py
    # You might want to remove this check if you in your future project want to be able to
    # enter bogus cpr numbers
    valid = valid and (cpr.checksum(input_cpr) == 0)
    return valid
```

Then we are able to test this validation function and see if it correctly
validates cpr numbers (and we do not neet to deal with how to test input).

*Rewrite the `get_*` functions from last week's solution so that they are testable and
by introduction of `validate_*` functions as described above.*

*Write tests for these functions.  Try with different values of input variables and assert False or True
depending on what you expect the output should be*


















