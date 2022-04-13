Suggested solution to Exercise 5_4:

Task:

*Create five additional classes: Course, CourseRequest, AdminPersonal, CourseResponsible and Teacher.
Course represents a university course, CourseRequest includes the request for a course on a given date.
AdminPersonal class represents an employee at an educational institution, 
Teacher is a class that represents an instructor in a university, and a course responsible is 
a special type of teacher, that on top of the responsibilities of a teacher, can request for course 
changes. 
AdminPersonal will have a set of course request to process, and can accept a course request 
or deny it.*

I will use this Exercise to introduce you to some methods that might be useful in your projects.

# MVC pattern

The program is build in a Model View Controller pattern. 

## Model
The requested classes are placed in a 'Model' folder
in order to get a better overview. Not all classes have been fully deployed as the solution is dependent on 
your various project solutions. However, the solution should give you an idea on howto make the class constructors,
use class inheritance, user properties, getters and setters etc.

The ActiveModel Class is a static class that holds the current state of the system - currently only the list of employees. It can
easily be expanded to hold the course list, the teacher list etc.

## View
The View is made with the ui files created in QT Designer. It consists of a Main Window which have a top menu,
and then there is a combobox menu in the left site and a stacked widget in the right part of screen.

MainWindowDescription.ui defines a widget with a simple text stating what you can do in the application

NewEmployee.ui defines a widget to add new employees to the system (we do not have a persistent layer yet, so
they will not be stored, when the application is closed). 

SearchEmployee.ui defines a widget with a search form, where you can search an employee by cpr number.
Pressing OK will make this the active/current employee in the ActiveModel class and can then e.g. be used
if you want to present a Course schedule for that employee... (for you to program)

![View](View.png)


## Controller

The Controller folder holds the classes which load the ui files from the view and handles the user input
and output.

The MainWindowGUI class loads the MainWindow.ui file and also instantiate the other widgets
and load them in the stacked widget.

The search- and add-employee forms can either be launched from the top menu or from the combobox menu.
From the top menu I have chosen to launch the forms in the stacked widget (for the exercise). 
From the combobox the forms are launched in their own windows (just to show that this can also be done).

# Summarization

Try to run the program and watch the console. Try to add some employees and see how the employees
are added to the Model. Search an employee and click ok. Watch how the Models active employee changes.

Several things are missing before this becomes a useful piece of software: e.g. check if there is
already a person with the same CPR-number in the system, when you add an employee.
But we now how a good starting point.











