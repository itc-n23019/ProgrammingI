def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_of_week(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29

    total_days = sum(days_in_month[:month - 1]) + day
    start_day = (total_days + year - 1 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7

    return start_day

def create_calendar(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29

    start_day = get_day_of_week(year, month, 1)

    cal = ""
    cal += f"{year}年 {month}月\n"
    cal += "日 月 火 水 木 金 土\n"

    cal += "   " * start_day

    day = 1
    for i in range(start_day, 7):
        cal += f"{day:2d} "
        day += 1

    cal += "\n"
    
    while day <= days_in_month[month - 1]:
        for i in range(7):
            if day <= days_in_month[month - 1]:
                cal += f"{day:2d} "
                day += 1
            else:
                cal += "   "
        cal += "\n"

    print(cal)

year = 2023
month = 8
create_calendar(year, month)

