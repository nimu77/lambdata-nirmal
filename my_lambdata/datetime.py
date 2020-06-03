# my_lambdata/datetime.py

class DateTime():
    def __init__(self, year, month, date, hour, minute, seconds):
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def timeline(self):
        print("It was", self.month, self.year)


if __name__ == "__main__":

    timeframe = DateTime(2020, "June", 3, 14, 59, 50)
    timeframe.timeline()

    timeframe2 = DateTime(1989, "May", 16, 4, 14, 19)
    timeframe2.timeline()
