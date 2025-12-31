def escalation_state():

    print("\n⚠️ I’m sorry — it looks like this issue needs human assistance.")
    print("I recommend contacting IT support or a technician for further help.")

    while True:
        choice = input("Would you like help with another issue? (yes / no): ").strip().lower()

        if choice == 'yes':
            return "CATEGORY_SELECTION"
        elif choice == 'no':
            return "END"
        else:
            print("Please answer with a yes or no")