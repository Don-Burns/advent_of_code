from dataclasses import dataclass
from typing import Self, TypeAlias

from aoc.logger import logger


def part_1(_input: str) -> int:
    # idea: find x in each line and scan in a circle for XMAS
    matrix = parse_input(_input)

    return search_target_word(matrix, "XMAS")


def part_2(_input: str) -> int:
    matrix = parse_input(_input)
    return search_target_word_in_cross(matrix, "MAS")


Matrix: TypeAlias = tuple[tuple[str, ...], ...]


def parse_input(_input: str) -> Matrix:
    return tuple(tuple(line) for line in _input.splitlines())


@dataclass
class MatrixBounds:
    i_max: int
    j_max: int
    i_min: int = 0
    j_min: int = 0

    @classmethod
    def from_matrix(cls, matrix: Matrix) -> Self:
        return cls(i_max=len(matrix[0]) - 1, j_max=len(matrix) - 1, i_min=0, j_min=0)

    def is_in_bounds(self, i: int, j: int) -> bool:

        return i >= 0 and j >= 0 and i <= self.i_max and j <= self.j_max


def search_target_word(data: Matrix, target_word: str) -> int:
    bounds = MatrixBounds.from_matrix(data)
    max_word_index = len(target_word) - 1
    count = 0
    for j, line in enumerate(data):
        for i, element in enumerate(line):
            # look for starting letter
            if element != target_word[0]:
                continue

            north = j - max_word_index
            south = j + max_word_index
            east = i + max_word_index
            west = i - max_word_index
            north_range = tuple(reversed(range(north, j + 1)))
            south_range = tuple(range(j, south + 1))
            east_range = tuple(range(i, east + 1))
            west_range = tuple(reversed(range(west, i + 1)))

            # search north
            if bounds.is_in_bounds(i, north):
                test = "".join(data[index][i] for index in north_range)
                if test == target_word:
                    logger.debug("Found north! i=%d, j=%d", i, j)
                    count += 1

            # search south
            if bounds.is_in_bounds(i, south):
                test = "".join(data[index][i] for index in south_range)
                if test == target_word:
                    count += 1
                    logger.debug("Found south! i=%d, j=%d", i, j)

            # search east
            if bounds.is_in_bounds(east, j):
                test = "".join(data[j][index] for index in east_range)
                if test == target_word:
                    count += 1
                    logger.debug("Found east! i=%d, j=%d", i, j)

            # search west
            if bounds.is_in_bounds(west, j):
                test = "".join(data[j][index] for index in west_range)
                if test == target_word:
                    count += 1
                    logger.debug("Found west! i=%d, j=%d", i, j)

            # search north east
            if bounds.is_in_bounds(east, north):
                test = "".join(data[_j][_i] for _i, _j in zip(east_range, north_range))
                if test == target_word:
                    count += 1
                    logger.debug("Found north east! i=%d, j=%d", i, j)

            # search south east
            if bounds.is_in_bounds(east, south):
                test = "".join(data[_j][_i] for _i, _j in zip(east_range, south_range))
                if test == target_word:
                    count += 1
                    logger.debug("Found south east! i=%d, j=%d", i, j)

            # search north west
            if bounds.is_in_bounds(west, north):
                test = "".join(data[_j][_i] for _i, _j in zip(west_range, north_range))
                if test == target_word:
                    count += 1
                    logger.debug("Found north west! i=%d, j=%d", i, j)

            # search south west
            if bounds.is_in_bounds(west, south):
                test = "".join(data[_j][_i] for _i, _j in zip(west_range, south_range))
                if test == target_word:
                    count += 1
                    logger.debug("Found south west! i=%d, j=%d", i, j)

    return count


def search_target_word_in_cross(data: Matrix, target_word: str) -> int:

    if len(target_word) % 2 == 0:
        raise ValueError("Word needs a center letter, so must be odd length")
    if len(target_word) > 3:
        # Note: might be fun to come back and do general case?
        raise NotImplementedError("Not implemented for words longer than 3 letters")

    center_letter = target_word[len(target_word) // 2]
    last_letter = target_word[-1]
    first_letter = target_word[0]
    count = 0
    for j, line in enumerate(data[1:-1], 1):
        for i, element in enumerate(line[1:-1], 1):
            # look for starting letter
            if element != center_letter:
                continue

            top_left = data[j - 1][i - 1]
            bottom_left = data[j + 1][i - 1]
            top_right = data[j - 1][i + 1]
            bottom_right = data[j + 1][i + 1]

            # both starting top
            if (
                top_left == first_letter
                and top_right == first_letter
                and bottom_left == last_letter
                and bottom_right == last_letter
            ):
                count += 1
            # both starting bottom
            if (
                top_left == last_letter
                and top_right == last_letter
                and bottom_left == first_letter
                and bottom_right == first_letter
            ):
                count += 1
            # both starting right
            if (
                top_right == first_letter
                and bottom_right == first_letter
                and top_left == last_letter
                and bottom_left == last_letter
            ):
                count += 1
            # both starting left
            if (
                top_left == first_letter
                and bottom_left == first_letter
                and top_right == last_letter
                and top_right == last_letter
            ):
                count += 1
    return count
