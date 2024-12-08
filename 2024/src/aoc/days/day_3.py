def part_1(_input: str) -> int:
    return process_mul_chunk(_input)


def part_2(_input: str) -> int:
    output = 0
    for do_dont in _input.split("do"):
        if do_dont.startswith("n't()"):
            continue
        output += process_mul_chunk(do_dont)

    return output


def process_mul_chunk(section: str) -> int:
    output = 0
    for sec in section.split("mul"):
        x, y, is_valid = parse_data_in_brackets(sec)
        if is_valid is False:
            continue
        output += x * y
    return output


def parse_data_in_brackets(data: str) -> tuple[int, int, bool]:
    _failing_case = 0, 0, False
    if data[0] != "(":
        return _failing_case
    # consume opening bracket
    data = data[1:]

    x, offset = consume_number(data)
    data = data[offset + 1 :]
    y, final_bracket_index = consume_number(data)
    if x is None or y is None or data[final_bracket_index] != ")":
        return _failing_case
    return x, y, True


def consume_number(data: str) -> tuple[int | None, int]:
    number_string: str = ""
    index_of_invalid_char = 0
    for index_of_invalid_char, char in enumerate(data):
        try:
            tmp = number_string + char
            int(tmp)
        except ValueError:
            break
        number_string = tmp

    if number_string == "":
        return None, index_of_invalid_char

    return int(number_string), index_of_invalid_char
