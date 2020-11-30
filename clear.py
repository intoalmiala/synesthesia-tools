clear = input("Would you like to clear played files and saved colors? [y/N] ")
if clear.lower() == "y":
    with open("played", "w") as f:
        print("Played files cleared.")
    with open("colors.json", "w") as f:
        print("Saved colors cleared.")

