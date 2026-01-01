from bot.states.start_state import start_state
from bot.states.category_state import category_state
from bot.states.issue_state import issue_details_state
from bot.states.troubleshoot import troubleshooting_state
from bot.states.escalation_state import escalation_state
from bot.states.resolution_state import resolution_state
from bot.states.end_state import end_state


def handle_state(current_state):

    if current_state == "START":
        # debug - print("FLOW CONTROLLER ENTERED START")
        next_state = start_state()
        return next_state

    elif current_state == "CATEGORY_SELECTION":
        next_state = category_state()
        return next_state

    elif current_state == "ISSUE_DETAILS":
        next_state = issue_details_state()
        return next_state

    elif current_state == "TROUBLESHOOTING":
        next_state = troubleshooting_state()
        return next_state

    elif current_state == "RESOLUTION":
        return resolution_state()

    elif current_state == "ESCALATION":
        return escalation_state()

    elif current_state == "END":
        return end_state()

    else:
        print("Unknown state. Returning to start.")
        return "START"
