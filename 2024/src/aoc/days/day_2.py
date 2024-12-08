from enum import Enum, auto
from typing import TypeAlias

Report: TypeAlias = tuple[int, ...]


class Part(Enum):
    PART_1 = auto()
    PART_2 = auto()


def part_1(_input: str) -> int:
    reports = parse_input(_input)
    return sum(int(is_report_safe(i, False)) for i in reports)


def part_2(_input: str) -> int:
    reports = parse_input(_input)
    return sum(int(is_report_safe(i, True)) for i in reports)


def parse_input(_input: str) -> list[Report]:
    return [tuple((int(i) for i in row.split(" "))) for row in _input.splitlines()]


class Direction(Enum):
    INCREASING = auto()
    DECREASING = auto()
    NEUTRAL = auto()


def is_report_safe(report: Report, with_dampening: bool) -> bool:
    prev: int | None = None
    prev_dir: Direction | None = None
    for i, cur in enumerate(report):
        # first value
        if i == 0:
            prev = cur
            continue
        if prev is None:
            raise RuntimeError(
                f"Previous None after first iter, should have been set by now. {report=}"
            )

        diff, cur_dir = check_level(prev, cur)

        if is_safe(prev_dir, diff, cur_dir) is False:
            if with_dampening is False:
                return False
            with_dampening = False
            # check what to use for next run out of the two values
            # next level needs to be valid with prev or current
            # not taking direction into account

            # Note: brute force method to ensure remove any 1 element will lead to pass
            # Not sure why just checking removing i - 1, i and i + 1 doesn't yield right
            # answer ¯\_(ツ)_/¯
            for index in range(len(report)):
                _report_without_failing_index = list(report)
                _report_without_failing_index.pop(index)
                without_index_is_safe = is_report_safe(
                    tuple(_report_without_failing_index), False
                )
                if without_index_is_safe is True:
                    return True
            return False

        prev = cur
        prev_dir = cur_dir

    return True


def is_safe(prev_dir: Direction | None, diff: int, cur_dir: Direction):
    # diff outside limits
    if abs(diff) > 3 or diff == 0:
        return False
    # direction changed
    if prev_dir != cur_dir and prev_dir is not None:
        return False
    return True


def check_level(prev: int, cur: int) -> tuple[int, Direction]:
    diff = prev - cur

    if diff == 0:
        cur_dir = Direction.NEUTRAL
    elif diff > 0:
        cur_dir = Direction.INCREASING
    else:
        cur_dir = Direction.DECREASING

    return diff, cur_dir
