from datetime import date, datetime


class DataValidator:

    @staticmethod   # This means that the method is static - it belongs to a class and not to an instance (object)
    def is_valid_date(date_string: str) -> bool:

        """
        A static method that checks if a string is valid date and in a valid format
        Use datetime.strftime() to define the format of the date being parsed.

        :param date_string:
        :return: bool
        """

        try:
            b = datetime.strptime(date_string , "%d/%m/%Y")
            print("caught date is:", b.strftime("%d/%m/%Y"))
            return True

        except:
            print("Illegal date:",date_string)
            return False
