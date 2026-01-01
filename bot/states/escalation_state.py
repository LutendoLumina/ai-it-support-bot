def handle_escalation(user_input: str) -> str:
    user_input = user_input.lower()

    if user_input == "yes":
        return "CATEGORY_SELECTION"
    elif user_input == "no":
        return "END"
    else:
        print("Please answer with a yes or no")
        return "ESCALATION"


def escalation_state():
    print("\n⚠️ I’m sorry — it looks like this issue needs human assistance.")
    print("Please contact IT support with the details you provided.")

    choice = input("Would you like help with another issue? (yes / no): ")

    return handle_escalation(choice)
