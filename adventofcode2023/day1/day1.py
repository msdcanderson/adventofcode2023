import re
from typing import List
from word2number import w2n

# from input import input

# from input_sample import input


class LineWithNumbersInAString:
    def __init__(self, line: str, pattern: str) -> None:
        self.line = line
        self.pattern = pattern
        self.numbers_in_line: List[str] = self.list_numbers_in_line()
        self.first_word: str = self.numbers_in_line[0]
        self.last_word: str = self.numbers_in_line[-1]

    def __str__(self) -> str:
        return self.line

    def list_numbers_in_line(self) -> List[str]:
        something = re.findall(self.pattern, self.line)
        # return re.findall(self.pattern, self.line)
        print(something)
        return something


def word_or_digit_to_digit(word: str, position: int) -> str:
    if word.isdigit():
        number_str = word
        return number_str[position]
    else:
        return str(w2n.word_to_num(word))


def process_line(line: str, pattern: str) -> int:
    line_object = LineWithNumbersInAString(line, pattern)
    first_digit: str = word_or_digit_to_digit(line_object.first_word, 0)
    print(first_digit)
    last_digit: str = word_or_digit_to_digit(line_object.last_word, -1)
    print(last_digit)
    calibration_value: int = int(first_digit + last_digit)
    return calibration_value


def main() -> None:
    # lines = ["atwo3b69","a1b"]
    lines = [
        "twooneightgt",
        "ddgjgcrssevensix37twooneightgt",
        "23eightptpspjtbnninesixfivedhfnmqjd",
    ]
    # convert input to a list of lines
    # lines: list[str] = input.splitlines()
    pattern: str = r"(\d+|one|two|three|four|five|six|seven|eight|nine)"

    sum_calibration_value: int = 0
    for line in lines:
        calibration_value = process_line(line, pattern)
        # print(calibration_value)
        sum_calibration_value += calibration_value
        # print(f"Line: {line}, First Digit: {first_digit}, Last Digit: {last_digit}, Calibration Value: {calibration_value}, Sum: {sum_calibration_value}")
        print(
            f"Line: {line}, Calibration Value: {calibration_value}, Sum: {sum_calibration_value}"
        )


if __name__ == "__main__":
    main()
