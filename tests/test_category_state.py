from bot.states.category_state import handle_category


def test_wifi_sentence_detected():
    assert handle_category("my wifi is not connecting") == "ISSUE_DETAILS"


def test_computer_slow_detected():
    assert handle_category("computer running very slow") == "ISSUE_DETAILS"


def test_invalid_input_returns_retry():
    assert handle_category("my screen is broken") == "CATEGORY_SELECTION"
