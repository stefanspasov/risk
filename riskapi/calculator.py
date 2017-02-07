from datetime import datetime

def calculateFailedLogins(dates, days):
    l = {k: v for k, v in dates if v == False and (datetime.now() - k).days <= days}
    return len(l)

def calculateHighestDate(dates, isLoginSuccess):
    l = {k: v for k, v in dates if v == isLoginSuccess}
    return max(l)