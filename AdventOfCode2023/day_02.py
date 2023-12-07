import re

with open("AdventOfCode2023/InputData/input_02.txt", "r") as file:
    games = [row.strip() for row in file.readlines()]


def part_one(input_list):
    """Q: What is the sum of the IDs of those games? (bag contains only 12 red, 13 green, and 14 blue or less)"""

    sum_of_ids = 0
    for game in input_list:
        game_id_string, game_rounds_string = game.split(":")
        game_id_num = int(game_id_string.split("Game ")[-1])
        game_rounds_list = [game_round.strip() for game_round in game_rounds_string.split(";")]

        max_red, max_blue, max_green = 0, 0, 0
        for game_round in game_rounds_list:
            # Find number of each colour cube:
            number_of_red = int(re.search(r"(\d{1,2}) red", game_round).group(1)) if "red" in game_round else 0
            number_of_blue = int(re.search(r"(\d{1,2}) blue", game_round).group(1)) if "blue" in game_round else 0
            number_of_green = int(re.search(r"(\d{1,2}) green", game_round).group(1)) if "green" in game_round else 0

            # See if number of colour cube is new max for the round (meaning it is min amount of colour in the bag):
            max_red = max(max_red, number_of_red)
            max_blue = max(max_blue, number_of_blue)
            max_green = max(max_green, number_of_green)

        # See if game passes given requirements:
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            sum_of_ids += game_id_num
    return sum_of_ids


def part_two(input_list):
    """Q: What is the sum of the power of these sets? (power = num_red * num_blue * num_green)"""
    all_games_power = 0
    for game in input_list:
        _, game_rounds_string = game.split(":")
        game_rounds_list = [game_round.strip() for game_round in game_rounds_string.split(";")]

        min_red, min_green, min_blue = 0, 0, 0
        for game_round in game_rounds_list:
            # Find number of each colour cube:
            red = int(re.search(r"(\d{1,2}) red", game_round).group(1)) if "red" in game_round else 0
            blue = int(re.search(r"(\d{1,2}) blue", game_round).group(1)) if "blue" in game_round else 0
            green = int(re.search(r"(\d{1,2}) green", game_round).group(1)) if "green" in game_round else 0

            # See if number of colour cube is new max for the round (meaning it is min amount of colour in the bag):
            min_red = max(min_red, red)
            min_blue = max(min_blue, blue)
            min_green = max(min_green, green)

        # Calculate the power of the game:
        single_game_power = min_red * min_blue * min_green
        all_games_power += single_game_power
    return all_games_power


print("-> Part One:", part_one(games))
print("-> Part Two:", part_two(games))
