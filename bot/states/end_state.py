def validate_rating(rating: str) -> bool:
    return rating.isdigit() and 1 <= int(rating) <= 5


def end_state():
    print("\n👋 Thank you for using SmartDesk Bot!")

    while True:
        rating = input("Before you go, please rate your experience (1–5): ").strip()

        if validate_rating(rating):
            print(f"\n⭐ Thank you for your feedback! You rated us {rating}/5.")
            break
        else:
            print("Please enter a number between 1 and 5.")

    print("\nGoodbye! Have a great day 😊")
    return None
