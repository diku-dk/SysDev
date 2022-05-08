class CourseLocation:
    """
    a Location for a University course
    """

    def __init__(self, location_id: str, address):
        self.__location_id = location_id
        self.__address = address

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address
