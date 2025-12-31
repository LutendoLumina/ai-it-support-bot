def start_state():

    # debug - print("START STATE CALLED")

    greeting = (
        "Hey there! 👋 Welcome to SmartDesk Bot.\n"
        "I can help you troubleshoot commom IT issues like Wi-Fi, printers, passwords and more.\n"
        "What do you need help with today?"
    )

    print(greeting)

    # Next state after greeting
    next_state = "CATEGORY_SELECTION"

    return next_state
