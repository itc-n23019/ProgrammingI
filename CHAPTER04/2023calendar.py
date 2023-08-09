import calendar
from termcolor import colored

def colored_calendar(year, month):
    c = calendar.TextCalendar(calendar.SUNDAY)
    cal = c.formatmonth(year, month)

    cal = cal.replace(" Sa", colored(" 土曜日", "blue"))
    cal = cal.replace("Su", colored("日曜日", "red"))

    print(cal)

year = 2023
month = 8
colored_calendar(year, month)

