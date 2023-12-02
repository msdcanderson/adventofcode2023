# import re

# # from typing import List
# from input import input

# # convert input to a list of lines
# lines = input.splitlines()

# # double check
# print(type(lines))
# print("lines")
# print(lines[0])

# # given a string, find the first number in the string
# # can be done using:
# # find(), findall(), regex, iterate through every character in string
# # use find all, then extract first and last number
# # https://www.codecademy.com/resources/docs/python/regex/findall

# # line = "1abc2"
# # line = "a1b2c3d4e5f"
# # line = "treb7uchet"
# line = "69sixthree6lxcrsevenseven69twonegs"
# # line = "eightwothree"

# pattern = r"\d+"
# pattern = r"(\d+|one|two|three|four|five|six|seven|eight|nine)"

# matches = re.findall(pattern, line)
# # matches: List[str] = re.findall(pattern, line)
# # digit can't be greater than 9
# print(line)
# print(matches)


# # # # find first number in line
# print(matches[0])

# from word2number import w2n

# # res = w2n.word_to_num(matches[0])
# # print(res)

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

# # # make sure number is between 1-9
# # # print(len(last_number))
# # # print(last_number[-1])
# # last_number = last_number[-1]

# # # # combine numbers
# # calibration_value: int = int(first_number + last_number)
# # print(calibration_value)
# # print(type(calibration_value))
