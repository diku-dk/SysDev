Suggested solution to Exercise Week 9,10 and 11:

Task:

*Bringing it all together: GUI, Model, Persistent data *


# Persistent Layer
A Layer for persistent storage (MySQL database) has been created in the `Persistent` folder.
It has been implemented as a Data Access Object pattern: https://en.wikipedia.org/wiki/Data_access_object.
I'm not a Software pattern export, but I guess a DAO must reside somewhere between a facade and
an adapter pattern.
The idea is to hide away the SQL commands from the upperlayer. They e.g. only see an `insert_employee()` method.
It has been implemented using interface classes using Python's abstract base class (ABC).

The DAO class describes the basic database methods like connect, setup and close
The EmployeeDAO class extends the DAO class and describes the methods needed to insert, update,
delete and search an employee or all employees.

The MySQLEmployeeDAO the implements all the methods.

You must make the same classes for other tables

The idea is that multiple database types can be supported - they will all have to implement
the DAO and xxxDAO classes.

`main.py` has been updated to recreate the database if is not there, to drop the table and recreate it and
insert som test data (setup()).

and then to show how to load and manipulate data.

The NewEmployeeGUI controller will now also add the new employee to the database (before it was just
added to the active model). What happens if the employee that you add already exists? You
must be able to handle such a situation in your code - e.g. with a try/except and catch
a uniqueness violation error.. - or by searching the entry before the insert takes place







