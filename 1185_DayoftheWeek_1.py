import datetime

class Solution:
    def dayOfTheWeek(self, day, month, year):
        """

        :param day: int
        :param month: int
        :param year: int
        :return: str
        """

        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


        return days[datetime.date(year,month,day).weekday()]
