import unittest
from user import *
from calculator import *
from datetime import datetime, timedelta

class calculatorTests(unittest.TestCase):
    def test_calculate_failed_logins(self):
        user1 = user("usr1")
        date1 = datetime.today() - timedelta(days=10)
        date2 = datetime.today() - timedelta(days=5)
        user1.addLoginDate(date1, True)
        user1.addLoginDate(date2, True)
        user1.addLoginDate(date2, False)

        result = calculateFailedLogins(user1.loginDates, 7)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()