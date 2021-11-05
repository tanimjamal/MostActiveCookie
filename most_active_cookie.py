"""
most_active_cookie module
<Summary>

Written by: Tanim Jamal
"""

import sys


class ActiveCookie:
    """This will output a list of most active cookies given a timestamp in the format of YYYY-MM-DD"""

    def __init__(self) -> None:
        """Keys that will be used to attain the occurrences of the cookie"""
        self.cookie_frequency = {}
        self.unique_cookies = set()

    def read_log(self, filename: str) -> None:
        """Function Header"""
        with open(filename, "r") as cookie_log:
            for line in cookie_log.readlines()[1:]:
                cookie, timestamp = line.rstrip().split(",")
                date, time = self.strip_date_and_time(timestamp)

                self.unique_cookies.add(cookie)

                if self.cookie_frequency.get((cookie, date)):
                    self.cookie_frequency[(cookie, date)].append(time)
                else:
                    self.cookie_frequency[(cookie, date)] = [time]


    def strip_date_and_time(self, timestamp: str) -> str:
        """Striping the date and time"""
        """Uses a string that gets the date of the year, month, and day format"""
        date, time = timestamp.split("T")
        return date, time

    def get_most_frequent_on_date(self, date: str) -> list:
        """Traverses through the frequencies of a specific date which then returns the cookies with the max occurences"""
        """ """
        most_frequent = []
        maximum_frequency = 0
        for cookie in self.unique_cookies:
            if self.cookie_frequency.get((cookie, date)):
                times = self.cookie_frequency.get((cookie, date))
                if maximum_frequency < len(times):
                    maximum_frequency = len(times)
                    most_frequent = [cookie]
                elif maximum_frequency == len(times):
                    most_frequent.append(cookie)


        return most_frequent


def main():
    """Main entrypoint of the most_active_cookie module"""
    if len(sys.argv) == 1 or len(sys.argv) < 4:
        print("The program needs arguments!")
        exit(1)  # exit with status code 1

    # Extract command, filename, option,
    # and option argument from system arguments
    filename, option, option_arg = sys.argv[1:]
    active_cookie = ActiveCookie()
    active_cookie.read_log(filename)

    if option == "-d":
        most_frequent = active_cookie.get_most_frequent_on_date(option_arg)
        for frequent_cookie in most_frequent:
            print(frequent_cookie)


if __name__ == "__main__":
    main()
