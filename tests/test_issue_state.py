from bot.states.issue_state import issue_details_state


def test_issue_state_moves_to_troubleshooting(monkeypatch):
    """
    Issue state should accept free-text input
    and always transition to TROUBLESHOOTING
    """

    # Mock user typing issue description
    monkeypatch.setattr("builtins.input", lambda _: "My computer shuts down randomly")

    next_state = issue_details_state()

    assert next_state == "TROUBLESHOOTING"
