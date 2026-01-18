def confirm_action(message="Confirm (Y/N): "):
    while True:
        choice = input(message).strip().lower()
        match choice:
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Please enter only Y or N")