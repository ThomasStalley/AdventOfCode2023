import re

with open("AdventOfCode2023/InputData/input_01.txt", "r") as file:
    unclean_calibrations = [row.strip() for row in file.readlines()]

# Mappings to replace string numbers with digits:
word_to_digit_crossover_mapping = {
    "oneight": "18",
    "threeight": "38",
    "fiveight": "58",
    "nineight": "98",
    "sevenine": "79",
    "twone": "21",
    "eighthree": "83",
    "eightwo": "82"
}
word_to_digit_singles_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
word_to_digit_mapping = word_to_digit_crossover_mapping | word_to_digit_singles_mapping


def part_one(input_list):
    total_calibration_p1 = 0
    for calibration in input_list:
        digits_only_string = "".join(re.findall(r"\d", calibration))
        partial_calibration_string = digits_only_string[0] + digits_only_string[-1]
        total_calibration_p1 += int(partial_calibration_string)
    return total_calibration_p1


def part_two(input_list):
    total_calibration_p2 = 0
    for calibration in input_list:
        for key in word_to_digit_mapping:
            calibration = calibration.replace(key, word_to_digit_mapping[key])
        numbers_list = re.findall(r"\d", calibration)
        partial_calibration_v2 = numbers_list[0] + numbers_list[-1]
        total_calibration_p2 += int(partial_calibration_v2)
    return total_calibration_p2


print("-> Part One:", part_one(unclean_calibrations))
print("-> Part Two:", part_two(unclean_calibrations))
