from bot.states.end_state import end_state


def test_end_state_accepts_valid_rating(monkeypatch):
    """
    End state should accept a rating between 1-5
    and exit cleanly.
    """

    # Simulate user entering a valid rating
    monkeypatch.setattr("builtins.input", lambda _: "4")

    end_state()
