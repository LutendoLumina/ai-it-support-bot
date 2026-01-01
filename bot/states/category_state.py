def handle_category(user_input: str) -> str:

    user_input = user_input.lower()

    # Rule-based matching
    if user_input == "1" or any(
        word in user_input for word in ["wifi", "wi-fi", "internet"]
    ):
        return "ISSUE_DETAILS"
    elif user_input == "2" or any(word in user_input for word in ["password", "reset"]):
        return "ISSUE_DETAILS"
    elif user_input == "3" or any(
        word in user_input for word in ["slow", "computer", "lag"]
    ):
        return "ISSUE_DETAILS"
    elif user_input == "4" or any(word in user_input for word in ["printer", "print"]):
        return "ISSUE_DETAILS"
    elif user_input == "5" or any(
        word in user_input for word in ["email", "login", "outlook"]
    ):
        return "ISSUE_DETAILS"
    else:
        print(
            "Sorry, I didn't quite understand that. Please choose one of the listed options."
        )
        return "CATEGORY_SELECTION"


def category_state():

    print("\nPlease select the issue you are facing: ")
    print("1: Wi-Fi not connecting")
    print("2. Password reset")
    print("3. Computer running slow")
    print("4. Printer not working")
    print("5. Email login issues")
    print("Type the number or describe the issue.")

    user_input = input("> ")

    return handle_category(user_input)
