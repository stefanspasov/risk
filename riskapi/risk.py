from flask import request
from flask import Flask
from repository import *
from user import *
from processLogResult import *
from logProcessor import *
from datetime import datetime
from calculator import *
app = Flask(__name__)

repo = None

@app.route('/log', methods=['POST'])
def log():
    global repo
    repo = repository()
    file = request.files['file']

    processLogResult = processLog(file)
    repo.addIp(processLogResult.ip)
    userExists = False
    for user in repo.users:
        if(user.name == processLogResult.name):
            user.addLoginDate(datetime.strptime(processLogResult.loginDate), processLogResult.isLoginSuccess)
            userExists = True
        break

    if(not userExists):
        newUser = user(processLogResult.name)
        newUser.addLoginDate(datetime.strptime(processLogResult.loginDate), processLogResult.isLoginSuccess)
        repo.addUser(newUser)


@app.route('/risk/isuserknown/<string:username>', methods=['GET'])
def isUserKnown(username):
    repo = repository()
    return repo.getUser(username)


@app.route('/risk/isipknown/<string:ip>', methods=['GET'])
def isIpKnown(ip):
    repo = repository()
    return ip in repo.ips


@app.route('/risk/failedloginlastweek/<string:username>', methods=['GET'])
def failedLoginLastWeek(username):
    repo = repository()
    user = repo.getUser(username)
    if (user is not None):
        return calculateFailedLogins(user.loginDates, 7)

    return None


@app.route('/risk/lastlogin/<string:username>/<bool:isSuccess>', methods=['GET'])
def lastFailedLogin(username, isSuccess):
    repo = repository()
    user = repo.getUser(username)
    if(user is not None):
        return calculateHighestDate(user.loginDates, isSuccess)

    return None




