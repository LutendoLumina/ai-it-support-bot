import bot.flow_controller as flow_controller


def test_start_state_routes_correctly(monkeypatch):
    def mock_start_state():
        return "CATEGORY_SELECTION"

    monkeypatch.setattr(flow_controller, "start_state", mock_start_state)

    next_state = flow_controller.handle_state("START")
    assert next_state == "CATEGORY_SELECTION"


def test_category_state_routes_correctly(monkeypatch):
    def mock_category_state():
        return "ISSUE_DETAILS"

    monkeypatch.setattr(flow_controller, "category_state", mock_category_state)

    next_state = flow_controller.handle_state("CATEGORY_SELECTION")
    assert next_state == "ISSUE_DETAILS"


def test_unknown_state_falls_back_to_start():
    next_state = flow_controller.handle_state("UNKNOWN_STATE")
    assert next_state == "START"
