def category_selection_state():
    print("\nPlease select the issue you are facing: ")
    print("1: Wi-Fi not connecting")
    print("2. Password reset")
    print("3. Computer running slow")
    print("4. Printer not working")
    print("5. Email login issues")
    print("Type the number or describe the issue.")

    user_input = input("> ").lower().strip()

    # Rule-based matching
    if user_input in ["1", "wifi", "wi-fi", "internet"]:
        return "ISSUE_DETAILS"
    elif user_input in ["2", "password", "reset"]:
        return "ISSUE_DETAILS"
    elif user_input in ["3", "slow", "computer", "lag"]:
        return "ISSUE_DETAILS"
    elif user_input in ["4", "printer",]:
        return "ISSUE_DETAILS"
    elif user_input in ["5", "email", "login"]:
        return "ISSUE_DETAILS"
    else:
        print("Sorry, I didn't quite understand that. Please choose one of the listed options.")
        return "CATEGORY SELECTION"