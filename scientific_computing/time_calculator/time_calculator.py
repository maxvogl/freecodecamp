def add_time(start, duration, day=None):

    """
    time_formating:
    splits "start" and "duration" into hours, minutes and day time (am/pm)
    """
    def time_formatting(time_string):
        time_split = time_string.split()
        hours, minutes = time_split[0].split(":")
        if len(time_split) == 1:
            return [hours, minutes]
        else:
            return [hours, minutes, time_split[1]]  # [hours, minutes, day time]

    """
    time_calculation
    calculates the new time and day time
    """

    def time_calculation(start_value, duration_value):
        if start_value[2] == "AM":
            dvalue1, hvalue1 = divmod(int(start_value[0]) + int(duration_value[0]), 24)
        else:
            dvalue1, hvalue1 = divmod(12 + int(start_value[0]) + int(duration_value[0]), 24)

        hvalue2, minutes = divmod(int(start_value[1]) + int(duration_value[1]), 60)
        dvalue2, hours = divmod(hvalue1 + hvalue2, 24)
        day_time, hours = divmod(hours, 12)
        days = dvalue1 + dvalue2
        if day_time == 0:
            day_time = "AM"
            if hours == 0:
                hours = 12
        else:
            day_time = "PM"
            if hours == 0:
                hours = 12
        return [days, hours, minutes, day_time]

    """
    str_formatting
    adds a "0" to the time string, if the length < 2 
    """

    def str_correction(value):
        if len(str(value)) < 2:
            return "0" + str(value)
        else:
            return str(value)

    # time = [days, hours, minutes, day time (AM/PM)]
    time = time_calculation(time_formatting(start), time_formatting(duration))
    new_time = str(time[1]) + ":" + str_correction(time[2]) + " " + time[3]

    # weekday calculation
    if not day == None:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        actual_day = 0
        while True:
            if day.lower() == weekdays[actual_day].lower():
                break
            actual_day += 1
        new_weekday = weekdays[((actual_day + (time[0] % 7)) % 7)]
        new_time = new_time + ", " + new_weekday

    if time[0] == 1:
        new_time = new_time + " (next day)"
    elif time[0] > 1:
        new_time = new_time + " (" + str(time[0]) + " days later)"

    return new_time
