def issue_details_state():

    print("\nThanks for that.")
    print("\nPlease describe the issue in a bit more detail:")

    user_input = input(">").strip()

    if not user_input:
        print("I didn't catch that. Could you please the issue?")
        return "ISSUE_DETAILS"
    
    print("\nGot it.")
    print("Let me look into the best way to help you with this")

    return "TROUBLESHOOTING"