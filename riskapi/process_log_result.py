class ProcessLogResult:

    def __init__(self, username, is_login_success, login_date, ip):
        self.username = username
        self.is_login_success = is_login_success
        self.login_date = login_date
        self.ip = ip