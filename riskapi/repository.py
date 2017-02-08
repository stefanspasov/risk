class Repository ():

    def __init__ (self):
        self.users = []
        self.ips = set()

    def add_user (self, user):
        self.users.append(user)

    def add_ip(self, ip):
        self.ips.add(ip)

    def get_user(self, username):
        for user in self.users:
            if user.name == username:
                return user