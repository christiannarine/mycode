def main():
    print("Welcome to the Basketball Player Matching Quiz!")
    print("Answer the following questions to find a basketball player who suits you.\n")

    while True:
        try:
            height = float(input("Enter your height in inches: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            position = input("What position do you prefer? (Guard/Forward/Center): ").capitalize()
            if position in ['Guard', 'Forward', 'Center']:
                break
            else:
                print("Invalid input. Choose from Guard, Forward, or Center.")
        except ValueError:
            print("Invalid input.")

    print("\nBased on your preferences, here are some basketball players who might suit you:\n")

    players = []

    if position == "Guard":
        players.append("Stephen Curry")
        players.append("Damian Lillard")
    elif position == "Forward":
        players.append("LeBron James")
        players.append("Kevin Durant")
    elif position == "Center":
        players.append("Joel Embiid")
        players.append("Nikola Jokic")

    if height < 72:
        players.append("Chris Clemons")
    elif 72 <= height < 80:
        players.append("Kawhi Leonard")
    else:
        players.append("Kristaps Porzingis")

    for player in players:
        print("- " + player)

if __name__ == "__main__":
    main()

