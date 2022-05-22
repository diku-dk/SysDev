from xml.dom.minidom import parseString
import jsonpickle
from dicttoxml import dicttoxml
from jsonpickle import json


class ObjectToXml:
    def __init__(self, myobject):
        self.myobject = myobject

    def to_xmlstring(self):
        # create a nested dictionary (by pickle to json and unpickle
        nested_dict = json.loads(jsonpickle.encode(self.myobject, unpicklable=False))
        # transform the dictionary to xml
        # notice the use of a custom function that removes the last letter of the parent nodes name
        # and uses it as item name. Eg courses -> course, students -> student
        def my_item_func(x): return x[:-1]
        xml_string = dicttoxml(nested_dict, root=False, item_func=my_item_func, attr_type=False)
        # generate pretty printed xml string using the parser from minidom
        return parseString(xml_string).toprettyxml(encoding="utf-8")

