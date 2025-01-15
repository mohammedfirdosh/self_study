class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # https://leetcode.com/problems/day-of-the-week
        if month < 3:
            month += 12
            year -= 1
        century = year // 100
        year = year % 100
        weekday = (century // 4 - 2 * century + year + year // 4 + 13 * (month + 1) // 5 + day - 1) % 7
        return [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ][weekday]
