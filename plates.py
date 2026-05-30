def main():
    plate = input("Plate: ").casefold().strip()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) <= 6 and len(s) >= 2 and str.isalpha(s):
        return True
    elif len(s) <= 6 and len(s) >= 2 and str.isalpha(s[0:2]) and s[2:3] is not "0" and str.isnumeric(s[2:6]):
        return True
    elif len(s) <= 6 and len(s) >= 2 and str.isalpha(s[0:3]) and s[2:3] != "0" and str.isnumeric(s[4:6]):
        return True

    else:
        return False



main()
