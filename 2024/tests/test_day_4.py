from textwrap import dedent

import pytest

from aoc.days import day_4 as d

TEST_INPUT = dedent(
    """\
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """
).strip("\n")


@pytest.fixture
def part_1_io() -> tuple[str, int]:
    return (TEST_INPUT, 18)


def test_part_1(part_1_io: tuple[str, int]):
    _input, expected = part_1_io

    assert d.part_1(_input) == expected


@pytest.mark.parametrize(
    ("input_", "expected"),
    (
        pytest.param(
            dedent(
                """\
                XMAS
                XMAS
                XMAS
                """
            ).strip("\n"),
            3,
            id="east",
        ),
        pytest.param(
            dedent(
                """\
                SAMX
                SAMX
                SAMX
                """
            ).strip("\n"),
            3,
            id="west",
        ),
        pytest.param(
            dedent(
                """\
                XXX
                MMM
                AAA
                SSS
                """
            ).strip("\n"),
            3,
            id="south",
        ),
        pytest.param(
            dedent(
                """\
                SSS
                AAA
                MMM
                XXX
                """
            ).strip("\n"),
            3,
            id="north",
        ),
        pytest.param(
            dedent(
                """\
                XAAA
                AMAA
                XXAA
                AAAS
                """
            ).strip("\n"),
            1,
            id="south east",
        ),
        pytest.param(
            dedent(
                """\
                AAAS
                AAAA
                AMAA
                XAAA
                """
            ).strip("\n"),
            1,
            id="north east",
        ),
        pytest.param(
            dedent(
                """\
                AAAX
                AAMA
                AAAA
                SAAA
                """
            ).strip("\n"),
            1,
            id="south west",
        ),
        pytest.param(
            dedent(
                """\
                AAAS
                AAAA
                AMAA
                XAAA
                """
            ).strip("\n"),
            1,
            id="north west",
        ),
        pytest.param(
            dedent(
                """\
                AAAA
                AAAA
                AAAA
                AAAA
                """
            ).strip("\n"),
            0,
            id="none",
        ),
    ),
)
def test_1_extended(input_: str, expected: int):
    assert d.part_1(input_) == expected


@pytest.fixture
def part_2_io() -> tuple[str, int]:
    input_ = dedent(
        """\
        .M.S......
        ..A..MSMS.
        .M.S.MAA..
        ..A.ASMSM.
        .M.S.M....
        ..........
        S.S.S.S.S.
        .A.A.A.A..
        M.M.M.M.M.
        ..........
        """
    ).strip()
    return (input_, 9)


def test_part_2(part_2_io: tuple[str, int]):
    _input, expected = part_2_io

    assert d.part_2(_input) == expected


@pytest.mark.parametrize(
    ("input_", "expected"),
    (
        pytest.param(
            dedent(
                """\
                MMM
                AAA
                SSS
                """
            ).strip("\n"),
            1,
            id="both top",
        ),
        pytest.param(
            dedent(
                """\
                SMM
                AAA
                SSM
                """
            ).strip("\n"),
            1,
            id="both right",
        ),
        pytest.param(
            dedent(
                """\
                SMS
                AAA
                MSM
                """
            ).strip("\n"),
            1,
            id="both bot",
        ),
        pytest.param(
            dedent(
                """\
                MAS
                AAA
                MAS
                """
            ).strip("\n"),
            1,
            id="both left",
        ),
        pytest.param(
            dedent(
                """\
                SAS
                AAA
                SAS
                """
            ).strip("\n"),
            0,
            id="Invalid, no M",
        ),
        pytest.param(
            dedent(
                """\
                MAS
                AAA
                SAM
                """
            ).strip("\n"),
            0,
            id="only horizontal matches",
        ),
        pytest.param(
            dedent(
                """\
                MSM
                ASA
                SSS
                """
            ).strip("\n"),
            0,
            id="only vertical matches",
        ),
    ),
)
def test_2_extended(input_: str, expected: int):
    assert d.part_2(input_) == expected
