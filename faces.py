def main():
    val = input("")
    print(convert(val))

def convert(n):

    return str(n).replace(":)", "🙂").replace(":(", "🙁")

main()
