def main():
    meal = input("What time is it? ")
    meal = convert(meal)

    if meal >= 7.0 and meal <=8.0:
        print("breakfast time")

    elif meal >= 12.0 and meal <=13.0:
        print("lunch time")

    elif meal >= 18.0 and meal <=19.0:
        print("dinner time")

    else:
        print("")


def convert(time):
    time = str(time).casefold()
    if "a.m." in time:
        time = time.rstrip("a.m.")
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        minutes = minutes / 60
        time = hours + minutes
        return time

    elif "p.m." in time:
        time = time.rstrip("p.m.")
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        minutes = minutes / 60
        time = (hours + minutes) + 12
        return time

    else:
         time = str(time)
         hours, minutes = time.split(":")
         hours = float(hours)
         minutes = float(minutes)
         minutes = minutes / 60
         time = hours + minutes
         return time

#line from the code structure you were given. That allows check50 to test your convert function separately. You’ll learn more about this in later weeks.
if __name__ == "__main__":

    main()
