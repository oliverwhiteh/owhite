# Get the user's input
deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().title()

match deep:
    case"42"|"Forty-Two"|"Forty Two":
        print("Yes")
    case _:
        print("No")



