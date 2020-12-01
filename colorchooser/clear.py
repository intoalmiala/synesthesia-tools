clear = input("Would you like to clear played files and saved colors? [y/N] ")
if clear.lower() == "y":
    with open("colors.json", "w") as f:
        f.write("{}")
        print("All data cleared.")

