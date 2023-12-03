import logging
import re

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Line:
    def __init__(self, line: str) -> None:
        self.line = line
        self.id = self.extract_number()

    def __str__(self) -> str:
        return f"Line: {self.line}, ID: {self.id}"

    def extract_number(self) -> int | None:
        match = re.search(r"Game (\d+):", self.line)
        if match:
            return int(match.group(1))
        else:
            return None


# # Example usage
# text = 'Game 2: 2 red, 4 blue, 3 green; 5 green, 3 red, 1 blue; 3 green, 5 blue, 3 red'
# number = extract_number(text)
# print(number)  # This should print '2'


line: str = (
    "Game 2: 2 red, 4 blue, 3 green; 5 green, 3 red, 1 blue; 3 green, 5 blue, 3 red"
)

line_object = Line(line)
logging.info(line_object)


# # Extracting the text before the first colon
# text_before_semicolon: str = line.split(':')[0]
# text_after_semicolon: str = line.split(':')[1]
# logging.debug(f"{text_before_semicolon} -> {text_after_semicolon}")
