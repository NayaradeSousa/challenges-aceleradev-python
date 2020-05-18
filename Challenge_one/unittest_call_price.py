import unittest
from main import calculate_call_price


class TestCase(unittest.TestCase):
    # 10:16:18 até 10:38:001586836758, 1586837747
    def test_basic_case(self):
        response = calculate_call_price(1586859378, 1586860680)
        self.assertEquals(2.25, response)

    # 22:10:33 até 22:15:49
    def test_basic_case2(self):
        response = calculate_call_price(1557969033, 1557969333)
        self.assertEquals(0.36, response)

    # 21:58:00 até 22:03:12
    def test_night_case(self):
        response = calculate_call_price(1557967762, 1557969442)
        self.assertEquals(1.35, response)

    # 05:59:18 até 06:15:47
    def test_day_case(self):
        response = calculate_call_price(1557996873, 1557997713)
        self.assertEquals(1.08, response)

    def test_83333333(self):
        response = calculate_call_price(1564704317, 1564707276)
        self.assertEquals(4.77, response)

    def test_49999999(self):
        response = calculate_call_price(1564610150, 1564610750)
        self.assertEquals(1.26, response)