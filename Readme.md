Suggested solution to Exercise Week 9,10 and 11:

Task:

*Bringing it all together: GUI, Model, Persistent data*



# Persistent Layer

Continuing on top of the solution for week 8, a Layer for persistent storage (MySQL database) has been added in the `Persistent` folder.
It has been implemented as a Data Access Object pattern: https://en.wikipedia.org/wiki/Data_access_object.
I'm not a Software pattern expert, but I guess a DAO must reside somewhere between a facade and
an adapter pattern.
The idea is to hide away the SQL commands from the upper layers so that they e.g. only see an `insert_employee()` method.
It has been implemented using interface classes using Python's abstract base class (ABC).

The DAO class describes the basic database methods like connect, setup and close.
The EmployeeDAO class extends the DAO class and describes the methods needed to insert, update,
delete and search an employee or all employees.

The MySQLEmployeeDAO implements all the methods defined in the interface classes.

You must make the same set of classes for other tables or implement a generic DAO.

The idea is that multiple database types can be supported - they will all have to implement
the DAO and xxxDAO classes.

`main.py` has been updated to recreate the database if is not there, to drop the table and recreate it and
insert som test data (setup()) and then to show how to load and manipulate data.

The NewEmployeeGUI controller will now also add the new employee to the database (before it was just
added to the active model). But what happens if the employee that you add already exists? You
must be able to handle such a situation in your code - e.g. with a try/except and catch
a uniqueness violation error.. - or by searching the entry before the insert takes place

Please note that the mysql.connector is set up using af pool of connections.
A connection is reused (if possible) for each query against a database. Only if the
database does not exist, a database-less connection is made, the database is created, and then
finally a new connection pool is set up.

Please also note the `cursor(dictionary=True)` which returns SQL queries in forms of dictionaries which
can easily be looped through.

PS! Some og the DAO methods prints the result to the console and returns a list at the same time.
It might need a cleanup!

Once the database has been set up, you could eg remove the statements in main that create and
manipulates the test entries. In your own application it could be nice if you created a
button to create the database and a button to load test data into the database.
This way you can control when to scratch all data and when to load test data.








