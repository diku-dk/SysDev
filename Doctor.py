class Doctor():
    def __init__(self,name, list_holidays):
        self.name = name
        self.list_holidays = list_holidays

    def __str__(self):
        return f"Name: {self.name}, Holidays: {self.list_holidays}"

