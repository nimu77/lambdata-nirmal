

import unittest
from my_lambdata.datetime import DateTime


class TestDateTime(unittest.TestCase):

    def test_datetime(self):

        timeframe = DateTime(2020, "June", 3, 14, 59, 50)
        self.assertEqual(timeframe.year, 2020)
        self.assertEqual(timeframe.hour, 14)


if __name__ == '__main__':
    unittest.main()
