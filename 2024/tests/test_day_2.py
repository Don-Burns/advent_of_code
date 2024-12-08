from textwrap import dedent

import pytest

from aoc.days import day_2 as d

TEST_INPUT = dedent(
    """\
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
).strip("\n")


@pytest.fixture
def part_1_io() -> tuple[str, int]:
    return (TEST_INPUT, 2)


def test_part_1(part_1_io: tuple[str, int]):
    _input, expected = part_1_io

    assert d.part_1(_input) == expected


@pytest.fixture
def part_2_io() -> tuple[str, int]:
    return (TEST_INPUT, 4)


def test_part_2(part_2_io: tuple[str, int]):
    _input, expected = part_2_io

    assert d.part_2(_input) == expected


@pytest.mark.parametrize(
    ("_input", "expected"),
    (
        pytest.param("1 2 3", 1),
        pytest.param("3 3 3", 0),
        pytest.param("3 2 1", 1),
        pytest.param("3 3 1", 1),
        pytest.param("1 3 3", 1),
        pytest.param("1 3 1", 1),
        pytest.param("1 3 1 3", 0),
        pytest.param("2 3 1", 1),
        pytest.param("1 2 3 4 5", 1),
        pytest.param("1 2 4 4 5", 1),
        pytest.param("5 5 3 1 0", 1),
        pytest.param("5 1 2 3 5", 1),
        pytest.param("1 5 4 4 5", 0),
        pytest.param("5 5 1 2 3", 0),
        # test input cases
        pytest.param("7 6 4 2 1", 1),
        pytest.param("1 2 7 8 9", 0),
        pytest.param("9 7 6 2 1", 0),
        pytest.param("1 3 2 4 5", 1),
        pytest.param("8 6 4 4 1", 1),
        pytest.param("1 3 6 7 9", 1),
    ),
)
def test_part_2_extra_cases(_input: str, expected: int):

    assert d.part_2(_input) == expected
