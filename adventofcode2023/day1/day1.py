import re
import logging
from word2number import w2n

from input_text import input_text

# from input_sample import input

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class LineWithNumbersInAString:
    DIGITS_PATTERN: str = r"(\d+)"
    NUMBERS_AS_WORDS_PATTERN: str = r"(one|two|three|four|five|six|seven|eight|nine)"  # task is for numbers between 1 and 9

    def __init__(self, line: str) -> None:
        self.line = line
        self.line_as_digits: str = self.convert_word_to_digit()
        self.numbers_in_line: list[str] = self.list_numbers_in_line()

    def __str__(self) -> str:
        return f"Line: {self.line}, Line as digits: {self.line_as_digits}, Numbers in line: {self.numbers_in_line}"

    def list_numbers_in_line(self) -> list[str]:
        numbers = re.findall(self.DIGITS_PATTERN, self.line_as_digits)
        logging.info(f"Numbers found in line: {numbers}")
        return numbers

    def convert_word_to_digit(self) -> str:
        line_as_digits = self.line
        for x in range(
            len(self.line) - 3
        ):  # longest word between one and nine is 3 char
            match = re.search(self.NUMBERS_AS_WORDS_PATTERN, line_as_digits)

            if match:
                # Replace the first occurrence of the matched pattern
                first_match = match.group(0)

                first_match_digit = str(w2n.word_to_num(first_match))

                match_minus_a_char = first_match[1:]

                line_as_digits = line_as_digits.replace(
                    first_match, first_match_digit + match_minus_a_char, 1
                )

                logging.debug(
                    f"{x} - Match: {first_match}, converted to: {first_match_digit}, Match minus a char: {match_minus_a_char}, Line as digits: {line_as_digits}"
                )
            else:
                break

        logging.info(f"Line as digits: {line_as_digits}")
        return line_as_digits


class LineProcessor(LineWithNumbersInAString):
    def __init__(self, line: str) -> None:
        super().__init__(line)

    @staticmethod
    def word_or_digit_to_digit(word: str, position: int) -> str:
        logging.debug(f"Processing word: {word} at position: {position}")
        if word.isdigit():
            number_str = word
            number_str_at_position = number_str[position]
            logging.debug(
                f"{word} is a digit, Number string at position {position}: {number_str_at_position}"
            )
            return number_str_at_position
        else:
            converted_number = str(w2n.word_to_num(word))
            logging.debug(
                f"{word} is not a digit, it's a word! It shouldn't happen, all the words should be numbers. Converted text to number: {converted_number}"
            )
            return converted_number

    def process(self) -> int:
        first_word: str = self.numbers_in_line[0]
        last_word: str = self.numbers_in_line[-1]
        first_digit: str = self.word_or_digit_to_digit(first_word, 0)
        logging.debug(f"First digit: {first_digit}")
        last_digit: str = self.word_or_digit_to_digit(last_word, -1)
        logging.debug(f"Last digit: {last_digit}")
        calibration_value: int = int(first_digit + last_digit)
        return calibration_value


def main() -> None:
    # lines = [
    #     "atwo3b69",
    #     "twooneightgt",
    #     "ddgjgcrssevensix37twooneightgt",
    #     "23eightptpspjtbnninesixfivedhfnmqjd",
    # ]
    # convert input to a list of lines
    lines: list[str] = input_text.splitlines()

    sum_calibration_value: int = 0
    for line in lines:
        logging.info(f"Line: {line}")

        line_processor = LineProcessor(line)
        # logging.debug(f"Line processor: {line_processor}")

        calibration_value = line_processor.process()
        logging.info(f"Calibration Value: {calibration_value}")

        sum_calibration_value += calibration_value
        logging.debug(f"Running total: {sum_calibration_value}")

    logging.info(f"Sum: {sum_calibration_value}")


if __name__ == "__main__":
    main()
