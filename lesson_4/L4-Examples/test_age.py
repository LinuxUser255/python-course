


def test_drink_age_can_drink(monkeypatch, capsys):
    """testing that a person 21 years old can drink alcohol."""
    # arrange th mock input to return '21'
    monkeypatch.setattr("builtins.input", lambda _: "21")

    # act: call the function we are testing
    from age import drink_age
    drink_age()

    # use assert to capture the output
    captured = capsys.readouterr()

    # assert that the output matches what we expect
    assert "You can drink." in captured.out
    assert captured.out == "You can drink.\n"


# testing that a person under 21 can't drink alcohol
def test_drink_age_cannot_drink(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "20")

    from age import drink_age
    drink_age()

    captured = capsys.readouterr()
    assert captured.out == "You can't drink.\n"""