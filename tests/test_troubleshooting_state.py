from bot.states.troubleshoot import troubleshooting_state


def test_troubleshoot_yes(monkeypatch):
    # Fake user input
    monkeypatch.setattr("builtins.input", lambda _: "yes")

    next_state = troubleshooting_state()

    assert next_state == "RESOLUTION"


def test_troubleshoot_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "no")

    next_state = troubleshooting_state()

    assert next_state == "ESCALATION"
