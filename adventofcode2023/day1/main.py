import re
from typing import List
from input import input

# convert input to a list of lines
lines = input.splitlines()


def prepare_calibration_value(line: str) -> int:
    matches: List[str] = re.findall(r"\d+", line)
    first_number: str = matches[0]
    first_number = first_number[0]
    last_number: str = matches[-1]
    last_number = last_number[-1]
    calibration_value: int = int(first_number + last_number)
    return calibration_value


sum_calibration_value = 0

for line in lines:
    calibration_value = prepare_calibration_value(line)
    sum_calibration_value += calibration_value

print(f"Calibration value: {sum_calibration_value}")
