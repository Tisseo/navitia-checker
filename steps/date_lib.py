

import datetime

def weekday_to_int(weekday):
    if weekday == "Lundi":
        return 0
    elif weekday == "Mardi":
        return 1
    elif weekday == "Mercredi":
        return 2
    elif weekday == "Jeudi":
        return 3
    elif weekday == "Vendredi":
        return 4
    elif weekday == "Samedi":
        return 5
    elif weekday == "Dimanche":
        return 6
    else :
        return 0

def next_weekday(d, weekday_int):
    """
    d est une date (datetime)
    weekday_int : 0 = lundi, 1 = mardi, etc
    exemple : next_monday = next_weekday(datetime.datetime.now(), 0) > retourne la date du prochain lundi
    """
    days_ahead = weekday_int - d.weekday()

    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def day_to_use (weekday, time):
    d = datetime.datetime.now()
    day_to_use = next_weekday(d, weekday_to_int(weekday))
    hour = int(time.split('h')[0])
    minute = int(time.split('h')[1])
    day_to_use = day_to_use.replace(hour = hour, minute = minute, second = 0).strftime("%Y%m%dT%H%M%S")
    return day_to_use
