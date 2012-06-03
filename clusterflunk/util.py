from datetime import datetime


def get_timedelta_string(dt):
    now = datetime.now()
    timedelt = now - dt

    # Printing logic
    if timedelt.days > 0:
        num = timedelt.days
        unit = "day"
    elif timedelt.seconds > 3600:
        num = timedelt.seconds / 3600
        unit = "hour"
    elif timedelt.seconds > 60:
        num = timedelt.seconds / 60
        unit = "minute"
    else:
        num = timedelt.seconds
        if num == 0:
            return "just created"
        unit = "second"

    plural = ""
    if num > 1:
        plural = "s"
    return "%s %s%s ago" % (str(num), unit, plural)
