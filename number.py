def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(promp):
    while True:
        try:
            return int(input(promp))
        except ValueError:
            pass

main()
