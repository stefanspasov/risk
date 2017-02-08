from process_log_result import *

def process_log(file_data):
    log_string = file_data.read()
    split_log_string = log_string.split("_")
    user_name = split_log_string[0]
    is_login_success = split_log_string[1]
    login_date = split_log_string[2]
    ip = split_log_string[3]
    return ProcessLogResult(user_name, is_login_success, login_date, ip)