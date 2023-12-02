import re
import logging
from word2number import w2n

# from input import input
# from input_sample import input

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class LineWithNumbersInAString:
    def __init__(self, line: str, pattern: str) -> None:
        self.line = line
        self.pattern = pattern
        self.numbers_in_line: list[str] = self.list_numbers_in_line()
        self.first_word: str = self.numbers_in_line[0]
        self.last_word: str = self.numbers_in_line[-1]

    def __str__(self) -> str:
        return self.line

    def list_numbers_in_line(self) -> list[str]:
        numbers = re.findall(self.pattern, self.line)
        logging.debug(f"Numbers found in line: {numbers}")
        return numbers


class LineProcessor(LineWithNumbersInAString):
    def __init__(self, line: str, pattern: str) -> None:
        super().__init__(line, pattern)

    @staticmethod
    def word_or_digit_to_digit(word: str, position: int) -> str:
        logging.debug(f"Processing word: {word} at position: {position}")
        if word.isdigit():
            logging.debug(f"{word} is a digit")
            number_str = word
            number_str_at_position = number_str[position]
            logging.debug(
                f"Number string at position {position}: {number_str_at_position}"
            )
            return number_str_at_position
        else:
            logging.debug(f"{word} is not a digit, it's a word!")
            converted_number = str(w2n.word_to_num(word))
            logging.debug(f"Converted text to number: {converted_number}")
            return converted_number

    def process(self) -> int:
        first_digit: str = self.word_or_digit_to_digit(self.first_word, 0)
        logging.debug(f"First digit: {first_digit}")
        last_digit: str = self.word_or_digit_to_digit(self.last_word, -1)
        logging.debug(f"Last digit: {last_digit}")
        calibration_value: int = int(first_digit + last_digit)
        return calibration_value


def main() -> None:
    lines = [
        "atwo3b69",
        "twooneightgt",
        "ddgjgcrssevensix37twooneightgt",
        "23eightptpspjtbnninesixfivedhfnmqjd",
    ]
    # convert input to a list of lines
    # lines: list[str] = input.splitlines()
    pattern: str = r"(\d+|one|two|three|four|five|six|seven|eight|nine)"

    sum_calibration_value: int = 0
    for line in lines:
        logging.info(f"Line: {line}")

        line_processor = LineProcessor(line, pattern)

        calibration_value = line_processor.process()
        logging.info(f"Calibration Value: {calibration_value}")

        sum_calibration_value += calibration_value
        logging.debug(f"Running total: {sum_calibration_value}")

    logging.info(f"Sum: {sum_calibration_value}")


if __name__ == "__main__":
    main()
