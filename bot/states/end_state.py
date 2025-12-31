from bot.utils import save_feedback

def end_state():

    print("\n👋 Thank you for using SmartDesk Bot!")

    while True:

        rating = input("Before you go, please rate your experience (1-5): ").strip()

        if rating.isdigit() and 1 <= int(rating) <= 5:
            save_feedback(int(rating))
            print(f"\n⭐ Thank you for your feedback! You rated us {rating}/5.")
            break
        else:
            print("Please enter a number between 1 and 5")

    print("\nGoodbye! 👋 Thank you for using smartDesk Bot. \nHave a great day 😊")
    return None

