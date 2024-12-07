from textwrap import dedent

import pytest

from aoc.days import day_1 as d


@pytest.fixture
def part_1_io() -> tuple[str, int]:
    return (
        dedent(
            """\
            3   4
            4   3
            2   5
            1   3
            3   9
            3   3
            """
        ).strip("\n"),
        11,
    )


def test_part_1(part_1_io: tuple[str, int]):
    _input, expected = part_1_io

    assert d.part_1(_input) == expected


@pytest.fixture
def part_2_io() -> tuple[str, int]:
    return (
        dedent(
            """\
            3   4
            4   3
            2   5
            1   3
            3   9
            3   3
            """
        ).strip("\n"),
        31,
    )


def test_part_2(part_2_io: tuple[str, int]):
    _input, expected = part_2_io

    assert d.part_2(_input) == expected
