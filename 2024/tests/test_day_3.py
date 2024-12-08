import pytest

from aoc.days import day_3 as d


@pytest.fixture
def part_1_io() -> tuple[str, int]:
    return (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
        161,
    )


def test_part_1(part_1_io: tuple[str, int]):
    _input, expected = part_1_io

    assert d.part_1(_input) == expected


@pytest.fixture
def part_2_io() -> tuple[str, int]:
    return (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
        48,
    )


def test_part_2(part_2_io: tuple[str, int]):
    _input, expected = part_2_io

    assert d.part_2(_input) == expected
