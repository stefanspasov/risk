import unittest
from user import *
from calculator import *
from datetime import datetime, timedelta

class CalculatorTests(unittest.TestCase):
    def test_calculate_failed_logins(self):
        user1 = User("usr1")
        date1 = datetime.today() - timedelta(days=10)
        date2 = datetime.today() - timedelta(days=5)
        user1.add_login_date(date1, True)
        user1.add_login_date(date2, True)
        user1.add_login_date(date2, False)

        result = calculate_failed_logins(user1.login_atempts, 7)
        self.assertEqual(result, 1)

    def test_calculate_latest_successful_date(self):
        login_atempts = []
        date1 = datetime.today() - timedelta(days=10)
        date2 = datetime.today() - timedelta(days=5)
        login_atempts.append((date1, True))
        login_atempts.append((date2, True))
        login_atempts.append((date1, False))

        result = calculate_latest_date(login_atempts, True)
        self.assertEqual(result, date2)

    def test_calculate_latest_unsuccessful_date(self):
        login_atempts = []
        date1 = datetime.today() - timedelta(days=10)
        date2 = datetime.today() - timedelta(days=5)
        login_atempts.append((date1, True))
        login_atempts.append((date2, True))
        login_atempts.append((date1, False))

        result = calculate_latest_date(login_atempts, False)
        self.assertEqual(result, date1)

if __name__ == '__main__':
    unittest.main()