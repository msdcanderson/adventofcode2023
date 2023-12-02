import re
import logging
from word2number import w2n

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

line = "9nineightwothree"
# line = 'twooneightgt'
pattern = r"(one|two|three|four|five|six|seven|eight|nine)"
# pattern: str = r"(one|two|three|four|five|six|seven|eight|nine)"

logging.debug(f"Line: {line}, length: {len(line)}")

for x in range(len(line) - 3):
    match = re.search(pattern, line)
    logging.debug(f"Match: {match}")
    if match:
        # Replace the first occurrence of the matched pattern
        first_match = match.group(0)

        first_match_digit = str(w2n.word_to_num(first_match))
        logging.debug(f"First match: {first_match}, converted to: {first_match_digit}")

        match_minus_a_char = first_match[1:]
        logging.debug(f"Match minus a char: {match_minus_a_char}")

        line = line.replace(first_match, first_match_digit + match_minus_a_char, 1)
        logging.debug(f"Line: {line}")

    else:
        break

logging.info(f"Line: {line}")

# from day1 import LineProcessor

# lines = [
#     "atwo3b69",
#     "twooneightgt",
#     "ddgjgcrssevensix37twooneightgt",
#     "23eightptpspjtbnninesixfivedhfnmqjd",
# ]
# # convert input to a list of lines
# # lines: list[str] = input.splitlines()
# pattern: str = r"(one|two|three|four|five|six|seven|eight|nine)"

# line = "twooneightgt"
# line_processor = LineProcessor(line, pattern)
# print(line_processor.convert_word_to_digit())
