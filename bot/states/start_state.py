def handle_start():
    return "CATEGORY_SELECTION"


def start_state():
    # debug - print("START STATE CALLED")

    print("Hey there! 👋 Welcome to SmartDesk Bot.\n")
    print(
        "I can help you troubleshoot commom IT issues like Wi-Fi, printers, passwords and more.\n"
    )
    print("What do you need help with today?")

    return handle_start()
