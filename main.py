from bot.flow_controller import handle_state

# debug - print("MAIN FILE STARTED")


def main():
    current_state = "START"

    while current_state is not None:
        # debug - print("MAIN LOOP STATE: ", current_state)

        current_state = handle_state(current_state)


if __name__ == "__main__":
    main()
