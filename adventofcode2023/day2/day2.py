import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Game:
    BALL_COLOURS: list[str] = ["red", "blue", "green"]

    def __init__(
        self,
        balls_in_bag: dict[str, int],
        first_clue: dict[str, int],
        second_clue: dict[str, int],
        third_clue: dict[str, int],
    ) -> None:
        self.balls_in_bag: dict[str, int] = balls_in_bag
        self.first_clue: dict[str, int] = first_clue
        self.second_clue: dict[str, int] = second_clue
        self.third_clue: dict[str, int] = third_clue

    def __str__(self) -> str:
        return f"In the bag there are {self.balls_in_bag}."

    @staticmethod
    def find_max_number(number1: int, number2: int, number3: int) -> int:
        largest_number: int = max(number1, number2, number3)
        return largest_number

    @staticmethod
    def extract_number_of_balls_by_colour_from_clue(
        dict_of_balls_by_colour: dict[str, int], colour: str
    ) -> int:
        # logging.debug(f"{colour} balls in bag: {dict_of_balls_by_colour[colour]}")
        return dict_of_balls_by_colour[colour]

    def extract_number_of_balls_by_colour(self, colour: str) -> tuple[int, int, int]:
        coloured_balls_first_clue: int = (
            self.extract_number_of_balls_by_colour_from_clue(self.first_clue, colour)
        )
        coloured_balls_second_clue: int = (
            self.extract_number_of_balls_by_colour_from_clue(self.second_clue, colour)
        )
        coloured_balls_third_clue: int = (
            self.extract_number_of_balls_by_colour_from_clue(self.third_clue, colour)
        )
        return (
            coloured_balls_first_clue,
            coloured_balls_second_clue,
            coloured_balls_third_clue,
        )

    @staticmethod
    def determine_bigger_number(number1: int, number2: int) -> str:
        if number1 > number2:
            return "possible"
        else:
            return "not possible"

    def process_colour(self, colour: str) -> str:
        number_of_balls_by_colour = self.extract_number_of_balls_by_colour(colour)
        logging.debug(
            f"Number of {colour} balls in the clues: {number_of_balls_by_colour}"
        )

        max_number_of_balls_by_colour_in_clues = self.find_max_number(
            number_of_balls_by_colour[0],
            number_of_balls_by_colour[1],
            number_of_balls_by_colour[2],
        )
        logging.debug(
            f"Max number of {colour} balls in the clues: {max_number_of_balls_by_colour_in_clues}"
        )
        logging.debug(type(max_number_of_balls_by_colour_in_clues))

        number_of_colour_balls_in_bag = (
            self.extract_number_of_balls_by_colour_from_clue(self.balls_in_bag, colour)
        )
        logging.debug(
            f"Number of {colour} balls in the bag: {number_of_colour_balls_in_bag}"
        )
        logging.debug(type(number_of_colour_balls_in_bag))

        largest_number = self.determine_bigger_number(
            number_of_colour_balls_in_bag, max_number_of_balls_by_colour_in_clues
        )
        logging.debug(f"{colour} is {largest_number}")
        return largest_number

    def process(self) -> None:
        possible = True
        for colour in self.BALL_COLOURS:
            if self.process_colour(colour) == "possible":
                possible = True
            else:
                possible = False
                break
        logging.info(f"It is possible the game could be played? {possible}")
        # return possible

    # get the number of balls in the bag by colour
    # find the max number for all reds, blues, and greens
    # compare the max numbers with balls in bag


def main() -> None:
    game1 = Game(
        balls_in_bag={"red": 10, "blue": 11, "green": 12},
        first_clue={"red": 1, "blue": 2, "green": 10},
        second_clue={"red": 4, "blue": 5, "green": 6},
        third_clue={"red": 7, "blue": 8, "green": 9},
    )
    logging.info(game1)
    # first_clue={"red": 1, "blue": 2, "green": 3}
    # logging.info(game1.extract_number_of_balls_by_colour_from_clue(first_clue,"red"))
    # logging.info(game1.extract_number_of_balls_by_colour(colour="red"))
    # game1.process(colour="red")
    # game1.process(colour="blue")
    # game1.process(colour="green")
    game1.process()

    # logging.info(game1.extract_number_of_balls_by_colour_from_clue("blue"))
    # logging.info(game1.extract_number_of_balls_by_colour_from_clue("green"))


if __name__ == "__main__":
    main()
