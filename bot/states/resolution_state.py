def handle_resolution(user_input: str) -> str:

    user_input = user_input.lower()

    if user_input == "yes":
        return "CATEGORY_SELECTION"

    elif user_input == "no":
        return "END"

    else:
        print("Please answer with a yes or no")
        return "RESOLUTION"


def resolution_state():

    print("\n🎉 Great news! Your issue has been resolved.")

    choice = input("Is there anything else I can help you with? (yes, no)\n> ")

    return handle_resolution(choice)
