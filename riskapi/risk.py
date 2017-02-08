from flask import request
from flask import Flask
from repository import *
from user import *
from process_log_result import *
from log_processor import *
from datetime import datetime
from calculator import *
app = Flask(__name__)

repo = Repository()

@app.route('/log', methods=['POST'])
def log():
    file = request.files['file']
    process_log_result = process_log(file)

    repo.add_ip(process_log_result.ip)

    user = repo.get_user(process_log_result.username)
    if user:
        user.add_login_date(datetime.strptime(process_log_result.login_date), process_log_result.is_login_success)

    else:
        new_user = User(process_log_result.username)
        new_user.add_login_date(datetime.strptime(process_log_result.login_date), process_log_result.is_login_success)
        repo.add_user(new_user)


@app.route('/risk/isuserknown/<string:username>', methods=['GET'])
def is_user_known(username):
    return repo.get_user(username)


@app.route('/risk/isipknown/<string:ip>', methods=['GET'])
def is_ip_known(ip):
    return ip in repo.ips


@app.route('/risk/failedloginslastweek/<string:username>', methods=['GET'])
def failed_logins_last_week(username):
    user = repo.get_user(username)
    if user:
        return calculate_failed_logins(user.login_atempts, 7)

    return "User not found"


@app.route('/risk/lastlogin/<string:username>/<bool:isSuccess>', methods=['GET'])
def last_login(username, isSuccess):
    user = repo.get_user(username)
    if user:
        return calculate_latest_date(user.login_atempts, isSuccess)

    return "User not found"