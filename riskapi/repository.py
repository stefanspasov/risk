class repository ():

    def __init__ (self):
        self.users = []
        self.ips = set()

    def addUser (self, user):
        self.users.append(user)

    def addIp(self, ip):
        self.ips.add(ip)

    def getUser(self, username):
        for user in self.users:
            if user.name == username:
                return user
        else:
            return None