# XML - example 2: flexible (and faster) solution (but more work)


In this example we will again have a `Student` class, a `Course` class (with som attributes - one them is a list of students) and a Courses class 
that is simply used to generate a list of courses.

the attributes for the `Student` are the same as before
```python
def __init__(self, first_name: str, last_name: str, cpr_number: str, phone: str, email: str):
```

like wise for the `Course` class

```python
def __init__(self, faculty: str, course_id: str, course_name: str, students: list):
```

and the `Courses` class.


Again our goal is to create an XML file that is used to share the information about courses and students:

This time the generated xml file will have the same structure, but the tag names will be different from
the internal object attribute names: (the quick observer might also have noticed that the indentation is different
from the previous example)

```xml
<?xml version='1.0' encoding='UTF-8'?>
<kurser>
  <kursus>
    <fakultet>DTU</fakultet>
    <kursusID>R080T</kursusID>
    <kursusnavn>Teknik for læger</kursusnavn>
    <studerende>
      <student>
        <fornavn>Anders</fornavn>
        <efternavn>Andersen</efternavn>
        <cpr_nummer>100181-0101</cpr_nummer>
        <telefon>+4512121212</telefon>
        <elpost>anders.andersen@company.com</elpost>
      </student>
      <student>
        <fornavn>Bente</fornavn>
        <efternavn>Bentsen</efternavn>
        <cpr_nummer>020282-0202</cpr_nummer>
        <telefon>+4566666666</telefon>
        <elpost>bente.bentsen@company.com</elpost>
      </student>
    </studerende>
  </kursus>
  <kursus>
    <fakultet>KU</fakultet>
    <kursusID>D0CT3R</kursusID>
    <kursusnavn>Sundhed for ingeniører</kursusnavn>
    <studerende>
      <student>
        <fornavn>Calle</fornavn>
        <efternavn>Callesen</efternavn>
        <cpr_nummer>020283-0203</cpr_nummer>
        <telefon>+4566666213</telefon>
        <elpost>calle.callesen@company.com</elpost>
      </student>
      <student>
        <fornavn>Ditte</fornavn>
        <efternavn>Dittesen</efternavn>
        <cpr_nummer>020280-0242</cpr_nummer>
        <telefon>+4534666213</telefon>
        <elpost>ditte.dittesen@company.com</elpost>
      </student>
    </studerende>
  </kursus>
</kurser>

```

Again we use the `dummyObjects` class to generate some test values.

## Introducing the xml generator and reader classes

This time we will create two classes which are specifically target at creating an xml file
from a `Courses` object and reading an xml file into a `Courses` object.

### Generating an XML file

`CoursesToXml` is the class that 'takes' your nested objects and 'turns' them into xml.
It uses etree and objectify from lxml and BytesIO from io in order to build xml file.
`Elements` is a 'helper' class with static methods that uses objectify in generate students and course
xml elements from their respective classes.
Note the flexibility - the internal attribute names are translated to the relevant XML
tag names (courses = kurser etc)


### Reading/Parsing an XML file

The `XmlToCourses` class' `parseXML()` method uses objectify in order to read the xml file
and translate it into `Courses` and `Students` objects.
Note the flexibility - the internal attribute names are translated to the relevant XML
tag names (courses = kurser etc)

## Putting it all together

Then `main.py` does the following (for demo purposes):

- creates some test objects
- write the test objects to xml (courses.xml - you can delete it before you execute main.py, and see that it is regenerated)
- reads the xml file back into objects 
- iterates over the objects and prints them
- validates xml files against a DTD file

### Validating the XML file

As before we will again try to validate the xml file against a DTD file.

Please notice that the dtd file has slightly changed from the previous example as
the indentation has changed. If you again use pycharm to generate the DTD file then 
please notice that you can change the indentation (here it has been changed from 4 to 2).

Again we use etree from the lxml library to read the dtd file and to validate an xml file against it.
The return value from `dtd.validate()` is a simple Boolean (True or False).

This time the `courses_invalid.xml` has two reasons for not being able to validate:
- the indentation is wrong
- it contains an element (car) that is not specified in the DTD
















