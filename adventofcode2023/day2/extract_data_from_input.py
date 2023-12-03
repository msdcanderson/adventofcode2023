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
        self.text_after_semicolon = self.line.split(":")[1]
        self.list_of_clues: list[str] = self.extract_clues()

    def __str__(self) -> str:
        return f"Line: {self.line}, ID: {self.id}, List of clues: {self.list_of_clues}"

    def extract_number(self) -> int | None:
        match = re.search(r"Game (\d+):", self.line)
        if match:
            return int(match.group(1))
        else:
            return None

    def extract_clues(self) -> list[str]:
        text_after_semicolon: str = self.line.split(": ")[1]
        list_of_clues_as_strings: list[str] = text_after_semicolon.split("; ")
        logging.info(list_of_clues_as_strings)
        return list_of_clues_as_strings


# # Example usage
# text = 'Game 2: 2 red, 4 blue, 3 green; 5 green, 3 red, 1 blue; 3 green, 5 blue, 3 red'
# number = extract_number(text)
# print(number)  # This should print '2'


line: str = (
    "Game 2: 2 red, 4 blue, 3 green; 5 green, 3 red, 1 blue; 3 green, 5 blue, 3 red"
)

line_object = Line(line)
logging.info(line_object)


# # # Extracting the text before the first colon
# text_before_semicolon: str = line.split(':')[0]
# text_after_semicolon: str = line.split(': ')[1]
# logging.info(f"{text_before_semicolon} -> {text_after_semicolon}")


text = "2 red, 4 blue, 3 green"
parts_of_text = text.split(", ")
clue = {}
for part in parts_of_text:
    logging.info(part)

    number = part.split(" ")[0]
    logging.info(number)

    colour = part.split(" ")[1]
    logging.info(colour)

    clue[colour] = int(number)
logging.info(clue)
