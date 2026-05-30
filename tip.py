def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # line 10 is for eliminate $
    d = str(d).strip("$")
    # line 12 is for convert the value to float
    d = float(d)
    #line 14 is to return the value to the function dollars...
    return d


def percent_to_float(p):
    #line 19 is for eliminate %
    p = str(p).strip("%")
    #line 21 is for convert the value to float and do the operation
    p = float(p) * 0.01
    #line 23 is to return the value to the function percent...
    return p


main()
