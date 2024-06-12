import pytest
from func import divide,greeting,multiply
@pytest.mark.parametrize(
    "x, y, result",
    [
        (5, 2, 2.5),
        (7, 2, 3.5),
        (100, 1, 100),
        (1,1,1)
    ],
)
def test_divide_success(x, y, result):
    assert divide(x, y) == result


@pytest.mark.parametrize(
    "x, y, result",
    [
        (2, 7, 4),
        (33, 3, 10),
        (100, 15, 4),
        (10, 80, 1),
        (3333, 88, 10),
        (100, 15, 4)
    ],
)
def test_divide_fail(x, y, result):
    assert divide(x, y) != result


def test_divide_exception():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize(
    "name, expected_output",
    [
        ("Alice", "Good morning, Alice!\n"),
        ("Bob", "Good morning, Bob!\n"),
        ("Charlie", "Good morning, Charlie!\n"),
        ("", "Good morning, !\n"),  # Test case for empty string
    ],
)
def test_greeting_success(name, expected_output, capsys):
    greeting(name)
    captured = capsys.readouterr()
    assert captured.out == expected_output

@pytest.mark.parametrize(
    "name, incorrect_output",
    [
        ("Alice", "Good morning, Bob!\n"),
        ("Bob", "Good morning, Alice!\n"),
        ("Charlie", "Good evening, Charlie!\n"),
        ("", "Good morning!\n"),  # Incorrect output for empty string
    ],
)
def test_greeting_fail(name, incorrect_output, capsys):
    greeting(name)
    captured = capsys.readouterr()
    assert captured.out != incorrect_output
def multiply(x: float, y: float) -> float:
    return x * y

@pytest.mark.parametrize(
    "x, y, result",
    [
        (5, 2, 10),
        (7, 2, 14),
        (100, 1, 100),
        (0, 1, 0),
        (-1, 5, -5),
        (2.5, 4, 10),
        (-3, -6, 18),
    ],
)
def test_multiply_success(x, y, result):
    assert multiply(x, y) == result

@pytest.mark.parametrize(
    "x, y, result",
    [
        (5, 2, 11),
        (7, 2, 15),
        (100, 1, 101),
        (0, 1, 1),
        (-1, 5, 5),
        (2.5, 4, 11),
        (-3, -6, 17),
    ],
)
def test_multiply_fail(x, y, result):
    assert multiply(x, y) != result