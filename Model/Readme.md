#The Model Folder
This folder holds the classes that define the System model.
It also holds a special static class (the activeModel) with class variables and methods.

This class can't be instantiated but can be used to keep the current 'state' of the whole system and can be
used to communicate/hold the state between the various part of the GUI.

Let us say that you search for a certain employee and later on (in another window/part of the gui) 
use the same employee to do something. Then you can e.g. save the information about which employee
is the active one. There are other means of 'communication' but this is one of them.

It is maybe not the 'pythonic' way of doing it - but this is also not a python course...