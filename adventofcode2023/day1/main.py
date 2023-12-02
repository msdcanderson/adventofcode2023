import re
from typing import List
from word2number import w2n
from input import input

# from input_sample import input


# convert input to a list of lines
lines = input.splitlines()


def number_by_position(list_of_numbers: List[str], position: int) -> str:
    number = list_of_numbers[position]
    return number


def convert_string_to_number(number: str) -> str:
    if number.isdigit():
        return number
    else:
        number = str(w2n.word_to_num(number))
        return number


def convert_string_to_single_number_as_string(matches: List[str], position: int) -> str:
    # print(matches)
    number: str = number_by_position(matches, position)
    # print(number)
    number = convert_string_to_number(number)
    # print(number)
    number = number[position]
    # print(number)
    # number: int = int(number)
    return number


pattern = r"(\d+|one|two|three|four|five|six|seven|eight|nine)"

sum_calibration_value = 0

for line in lines:
    matches: List[str] = re.findall(pattern, line)

    first_number: str = convert_string_to_single_number_as_string(matches, 0)
    # print(first_number)

    last_number: str = convert_string_to_single_number_as_string(matches, -1)
    # print(last_number)

    calibration_value: int = int(first_number + last_number)
    # print(calibration_value)

    sum_calibration_value += calibration_value
    print(
        f"line: {line} - first number: {first_number} - last number: {last_number} - calibration value: {calibration_value} - sum: {sum_calibration_value}"
    )

print(f"Calibration value: {sum_calibration_value}")


# print(convert_string_to_single_number_as_string(matches, 1))


# first_number_in_string: str = number_by_position(matches, position)
# print(first_number_in_string)
# first_number_in_string: str = convert_string_to_number(first_number_in_string)
# print(type(first_number_in_string))
# get_first_number = first_number_in_string[position]
# print(get_first_number)


# number = number_by_position(matches, -1)
# print(number)
# number = convert_string_to_integer(number)
# # make sure number is between 1-9
# number = number[0]
# print(number)


#     first_number: str = matches[0]
#     first_number = first_number[0]
#     last_number: str = matches[-1]
#     last_number = last_number[-1]
#     calibration_value: int = int(first_number + last_number)
#     return calibration_value


# sum_calibration_value = 0

# for line in lines:
#     calibration_value = prepare_calibration_value(line)
#     sum_calibration_value += calibration_value

# print(f"Calibration value: {sum_calibration_value}")


# print(number


# first_number: str = matches[0]
# print(first_number)

# if first_number.isdigit():
#     print("true")
#     # make sure number is between 1-9
#     first_number = first_number[0]
#     print(first_number)
# else:
#     first_number: str = w2n.word_to_num(matches[0])
#     print(first_number)

#     # # find last number in line
#     # print(matches[-1])

# last_number: str = matches[-1]
# print(last_number)
# if last_number.isdigit():
#     print("true")
#     # make sure number is between 1-9
#     last_number = last_number[-1]
#     print(last_number)
# else:
#     last_number: str = w2n.word_to_num(matches[-1])
#     print(last_number)
