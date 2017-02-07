from procesLogResult import *

def processLog(fileData):
    logString = fileData.read()
    splitLogString = logString.split("_")
    userName = splitLogString[0]
    isLoginSuccess = splitLogString[1]
    loginDate = splitLogString[2]
    ip = splitLogString[3]
    return processLogResult(userName, isLoginSuccess, loginDate, ip)