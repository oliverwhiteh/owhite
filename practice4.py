def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            recommend("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else:
        recommend("Enter a valid difficulty")



def recommend(game):
    print("You might like", game)


main()
