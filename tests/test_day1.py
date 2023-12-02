import pytest
from adventofcode2023.day1.day1 import LineWithNumbersInAString


class TestLineWithNumbersInAString:
    pattern: str = r"(\d+|one|two|three|four|five|six|seven|eight|nine)"

    @pytest.mark.parametrize(
        "line, expected",
        [
            # Add test cases here:
            ("twooneightgt", ["two", "one", "eight"]),
            (
                "ddgjgcrssevensix37twooneightgt",
                ["seven", "six", "37", "two", "one", "eight"],
            ),
            ("eightwothree", ["eight", "two", "three"]),
            ("29", ["29"]),
        ],
    )  # type: ignore
    def test_list_numbers_in_line(self, line: str, expected: list[str]) -> None:
        line_with_numbers = LineWithNumbersInAString(line, self.pattern)
        assert line_with_numbers.list_numbers_in_line() == expected
