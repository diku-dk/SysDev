class Clinic:
    def __init__(self, name: str,address: str, list_holidays: [], list_doctors: []):
        self.name = name
        self.address = address
        self.list_holidays = list_holidays
        self.list_doctors = list_doctors

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Holidays: {self.list_holidays}, Doctors: {self.list_doctors}"

