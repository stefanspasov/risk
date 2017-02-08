from datetime import datetime


def calculate_failed_logins(dates, days):
    if not isinstance(dates, list):
        raise Exception("Expected a dict type")
    return len([False for login_date, success in dates
                if not success and (datetime.now() - login_date).days <= days])

def calculate_latest_date(dates, is_login_success):
    if not isinstance(dates, list):
        raise Exception("Expected a dict type")
    return max([k for k, success in dates if success == is_login_success])
