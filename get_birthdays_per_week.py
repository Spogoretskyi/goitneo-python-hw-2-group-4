from collections import defaultdict
from datetime import datetime


def get_day(date):
    return date.strftime("%A")


def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    current_year = datetime.today().year
    current_date = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = current_year)

        if birthday_this_year < current_date:
            birthday_this_year.replace(year = current_year + 1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7 and delta_days > 0:
            day = get_day(user["birthday"])

            if day in ("Saturday", "Sunday"):
                day = "Monday"
            
            birthdays_per_week[day].append(name)

    return birthdays_per_week
    

