# XML - example 1: quick, dirty and inflexible

XML stands for Extensible Markup Language and is (still) one of the data formats most frequently used for exchange of data between systems. 
Other examples (among many) of data exchange formats are JSON, YAML and CSV.

You will need to generate XML files from your systems internal objects.

In this example we have a `Student` class, a `Course` class (with som attributes - one them is a list of students) and a Courses class 
that is simply used to generate a list of courses.

In a 'final' solution we would store all this information in a database and then read the database records into objects whenever needed.
The objects can then be used in classes and methods to either be presented in a GUI
or written to e.g. and XML file.

the attributes for the `Student` class can be seen in the constructor
```python
def __init__(self, first_name: str, last_name: str, cpr_number: str, phone: str, email: str):
```

like wise for the `Course` class

```python
def __init__(self, faculty: str, course_id: str, course_name: str, students: list):
```

and the `Courses` class just 'generates' a list to which we can append courses.


Our goal is to create an XML file that is used to share the information about courses and students:

The XML file can best be described as a tree: The root is here "courses". Then you have a trunk for each course and branches/leaves for each student 

So the XML file we are aiming for would look something like:

```xml
<?xml version="1.0" encoding="utf-8"?>
<courses>
	<course>
		<faculty>DTU</faculty>
		<courseID>R080T</courseID>
		<courseName>Teknik for læger</courseName>
		<students>
			<student>
				<first_name>Anders</first_name>
				<last_name>Andersen</last_name>
				<cpr_number>100181-0101</cpr_number>
				<phone>+4512121212</phone>
				<email>anders.andersen@company.com</email>
			</student>
			<student>
				<first_name>Bente</first_name>
				<last_name>Bentsen</last_name>
				<cpr_number>020282-0202</cpr_number>
				<phone>+4566666666</phone>
				<email>bente.bentsen@company.com</email>
			</student>
		</students>
	</course>
	<course>
		<faculty>KU</faculty>
		<courseID>D0CT3R</courseID>
		<courseName>Sundhed for ingeniører</courseName>
		<students>
			<student>
				<first_name>Calle</first_name>
				<last_name>Callesen</last_name>
				<cpr_number>020283-0203</cpr_number>
				<phone>+4566666213</phone>
				<email>calle.callesen@company.com</email>
			</student>
			<student>
				<first_name>Ditte</first_name>
				<last_name>Dittesen</last_name>
				<cpr_number>020280-0242</cpr_number>
				<phone>+4534666213</phone>
				<email>ditte.dittesen@company.com</email>
			</student>
		</students>
	</course>
</courses>

```

The process for going from the internal object representation to an XML file is often referred to (especially in Java) as 'Marshalling' og 'XML serialization'.
In Python there are many ways of achieving this goal. One of them is presented in the attached marshalling.zip file in week 12's lecture: https://absalon.ku.dk/courses/56610/modules/items/1647267

We will here present two slightly alternative methods.

The first - 'quick and dirty' - method will use the internal object and attribute names as tag and attribute names in you final XML file.  

This means that if you code uses the attribute name "karakterer", then that will also be used as the attribute name in the generated XML file.
And if you e.g. have used `__` to make the attributes private, then this will also show up in your generated XML file.
Of course this is not very flexible  - and hence close to unusable - in a real system.

On flexible thing though, is that the method has no knowledge about the names of the object attributes og tag names 

Several 'tricks' are used in the method. E.g. (a)busing that objects (can) have an internal dictionary representation in Python.
Another 'funny' thing about this method is that it temporarily uses json as format, as json representation is build into Python.


However, the method can be used to give a first explanation and good overview the process of going forth and back from objects to XML!


## Introducing some more classes

Three more classes are needed.

The `dummyObjects` class is just a static class with a static method that returns a list of courses
for which each hold a list of students.
You would have a similar list in your project that you would like to export; it could e.g. be that you have list of course change requests that 
again might have requests for several days or locations... (I guess you get the point)

The two other classes are the ones actually performing all the work:

### Generating an XML file

`ObjectToXml` is the class that 'takes' your nested objects and 'turns' them into xml.
It uses jsonpickle (https://jsonpickle.github.io/) in order to create a json representation.
then it immediately loads the json representation into a nested dictionary. It then uses
dicttoxml in order to turn the nested dictionary into xml. Finally, it uses
parseString from xml.dom.minidom to 'prettyprint' the xml string into a nice and human-readable XML file.
The `my_item_func(x)` used in dicttoxml removes the last letter of the parent nodes name and uses it as item name.
Otherwise, each item (course or student) would just have been tagged with `<item>` and not e.g. `<student>`.

### Reading/Parsing an XML file

The XmlToObject.py holds three classes: `XmlToObject` which does the work and then to small helper classes `Obj` and `Helper`
which are used by XmlToObject. XmlToObject uses xmltodict which - surprisingly - can generate a nested dictionary
from XML. And then it uses json as middle-station (the `dict2obj()` method) in the reverse process of ObjectToXml 

## Putting it all together

Then `main.py` does the following (for demo purposes):

- creates some test objects
- write the test objects to xml (courses.xml - you can delete it before you execute main.py, and see that it is regenerated)
- reads the xml file back into objects 
- iterates over the objects and prints them
- validates xml files against a DTD file

### Validating the XML file

The final lines in the main.py files show how to use a DTD (Document type definition) file to validate the xml
files. You can read a little more about DTD here: https://www.w3schools.com/xml/xml_dtd.asp

Pycharm is able to generate the DTD file for you (from an XML file):
Open you xml file.
Under tools-> XML Actions -> Generate Schema from XML file -> select DTD and the output destination.

The `courses.dtd` file is generated this way

We then uses etree from the lxml library to read the dtd file and to validate an xml file against it.
The return value from `dtd.validate()` is a simple Boolean (True or False).

`courses_invalid.xml` has been tampered with: The attribute/tag `<car>BMW</car>` has been added.
Therefore, the XML file doesn't pass the validation against the DTD file!
















