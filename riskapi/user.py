class User:

    def __init__(self, name):
        self.name = name
        self.login_atempts = []

    def add_login_date(self, date, is_success):
        self.login_atempts.append((date, is_success))