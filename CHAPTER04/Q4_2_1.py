def number_to_day(num=0):
    if num == 0 or None:
        day = "今日"
    elif num == 1:
        day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より１日を超えて離れた日"

