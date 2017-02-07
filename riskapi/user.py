class user:

    def __init__(self, name):
        self.name = name
        self.loginDates = {}

    def addLoginDate(self, date, isSuccess):
        self.loginDates[date] = isSuccess