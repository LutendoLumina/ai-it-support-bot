def resolution_state():

    print("\n🎉 Great news! Your issue has been resolved.")

    while True:
        choice = input("Is there anything else I can help you with? (yes, no): ").strip().lower()

        if choice == 'yes':
            return "CATEGORY_SELECTION"
        elif choice == 'no':
            return "END"
        else:
            print("Please answer with a yes or no")

