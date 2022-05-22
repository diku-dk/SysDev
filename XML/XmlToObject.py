import xmltodict
import json


class Helper:
    '''
    Helper class with static method to convert dict to object
    '''
    @staticmethod
    def dict2obj(d):
        return json.loads(json.dumps(d), object_hook=Obj)


class Obj(object):
    '''
    class to use as object_hook in json.loads
    '''
    def __init__(self, dict_):
        self.__dict__.update(dict_)


class XmlToObject:

    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def to_object(self):
        # parse the xml
        with open(self.xml_filename, "rb") as fd:
            dictionary = xmltodict.parse(fd.read())
            print("Generated dictionary from the XML file:\n", dictionary)
            return Helper.dict2obj(dictionary)


