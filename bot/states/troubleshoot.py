def troubleshooting_state():

    print("\nLet's try a few quick troubleshooting steps.")

    print("\nStep 1: ")
    print("• Restart the affected device or service.")
    print("• Check all cables and connections.")
    print("• Ensure the device is powered on.")

    while True:

        user_input = input("Did this resolve your issue? (yes / no) \n> ").strip().lower()

        if user_input in ("yes", "y"):
            return "RESOLUTION"
        
        elif user_input in ("no", "n"):
            print("\nThanks for confirming. \n")
            return "ESCALATION"
        
        
        print("Sorry, please answer with a yes or no. \n")