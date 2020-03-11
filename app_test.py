
from app import generate_integers


def test_generate_integers_length() -> None:
    integers = generate_integers(1, 10, 2)
    assert len(integers) == 5, "The list should contain 5 numbers"


def test_generate_integers_start_and_stop() -> None:
    integers = generate_integers(1, 10, 2)
    assert 1 in integers, "1 should be in the list of integers"
    assert 10 not in integers, "10 should be in the list of integers"


def test_generate_integers_step() -> None:
    integers = generate_integers(1, 10, 2)
    assert all(n in integers for n in (1, 3, 5, 7, 9)), f"{integers} should be contain all of (1, 3, 5, 7, 9)"


# def test_generate_integers_fail():
#     integers = generate_integers(1, 10, 2)
#     assert len(integers) > 20, "The list should ocntain more than 20 elements"
