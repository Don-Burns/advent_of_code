from collections import Counter


def part_1(_input: str) -> int:
    left_list, right_list = split_input(_input)
    left_list.sort()
    right_list.sort()
    output: int = 0
    for left, right in zip(left_list, right_list, strict=True):
        output += abs(left - right)

    return output


def part_2(_input: str) -> int:
    lhs, rhs = split_input(_input)
    rhs_counter = Counter(rhs)

    output: int = 0
    for val in lhs:
        output += rhs_counter.get(val, 0) * val

    return output


def split_input(_input: str) -> tuple[list[int], list[int]]:
    left_list: list[int] = []
    right_list: list[int] = []
    for line in _input.splitlines():
        left, right = (int(i) for i in line.split("   "))  # 3 spaces?
        left_list.append(left)
        right_list.append(right)

    return left_list, right_list
