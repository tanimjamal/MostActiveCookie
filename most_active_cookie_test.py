"""
Testing module for most_active_cookie.py
"""

# running command: python -m unittest most_active_cookie_test.py
# CSV File does not exist
# There's no date
# There's no data in the csv file

import unittest
from most_active_cookie import ActiveCookie


class ActiveCookieTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_get_most_frequent_on_date(self):
        active_cookie = ActiveCookie()
        active_cookie.read_log("cookie_log.csv")
        # this test ensures when "2018-12-09" is tested, only "AtY0laUfhglK3lC7" should be outputed
        self.assertEquals(
            active_cookie.get_most_frequent_on_date("2018-12-09"), ["AtY0laUfhglK3lC7"]
        )
        # this test ensures when "2018-12-08" is tested, only "AtY0laUfhglK3lC7" should be outputed
        self.assertCountEqual(
           active_cookie.get_most_frequent_on_date("2018-12-08"), ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        )
        # this test ensures when "2018-12-07" is tested, only "AtY0laUfhglK3lC7" should be outputed
        self.assertEquals(
            active_cookie.get_most_frequent_on_date("2018-12-07"), ["4sMM2LxV07bPJzwf"]
        )
        # this test ensures when "2018-12-06" is tested,
        # nothing should be outputted since that date does not exist in the file
        self.assertEquals(
            active_cookie.get_most_frequent_on_date("2018-12-06"), []
        )
        # this test ensures when "2018" is tested,
        # nothing should be outputted since that date does not exist and it is not the expected format
        self.assertEquals(
            active_cookie.get_most_frequent_on_date("2018"), []
        )
        # this test ensures when nothing is inputted, it returns an argument saying "The program needs arguments!"
        #self.assertEquals(
        #    active_cookie.get_most_frequent_on_date(""), ["The program needs arguments!"]
        #)

if __name__ == "__main__":
    unittest.main()
