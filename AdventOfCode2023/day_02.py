import re

with open("AdventOfCode2023/InputData/input_02.txt", "r") as file:
    games = [row.strip() for row in file.readlines()]


def _get_min_colours(rounds):
    min_red, min_blue, min_green = 0, 0, 0
    for game_round in rounds:
        # Find number of each colour cube:
        number_of_red = int(re.search(r"(\d{1,2}) red", game_round).group(1)) if "red" in game_round else 0
        number_of_blue = int(re.search(r"(\d{1,2}) blue", game_round).group(1)) if "blue" in game_round else 0
        number_of_green = int(re.search(r"(\d{1,2}) green", game_round).group(1)) if "green" in game_round else 0

        # See if number of colour cube is new max for the round (meaning it is min amount of colour in the bag):
        min_red = max(min_red, number_of_red)
        min_blue = max(min_blue, number_of_blue)
        min_green = max(min_green, number_of_green)
    return min_red, min_blue, min_green


def part_one(input_list):
    sum_of_ids = 0
    for game in input_list:
        game_id_string, game_rounds_string = game.split(":")
        game_id_num = int(game_id_string.split("Game ")[-1])
        game_rounds_list = [game_round.strip() for game_round in game_rounds_string.split(";")]
        min_red, min_blue, min_green = _get_min_colours(game_rounds_list)

        # See if game passes given requirements, if so add game id to sum of ids:
        sum_of_ids += game_id_num if min_red <= 12 and min_blue <= 13 and min_green <= 14 else 0
    return sum_of_ids


def part_two(input_list):
    all_games_power = 0
    for game in input_list:
        _, game_rounds_string = game.split(":")
        game_rounds_list = [game_round.strip() for game_round in game_rounds_string.split(";")]
        min_red, min_blue, min_green = _get_min_colours(game_rounds_list)

        # Calculate the power of the single game, add to total power:
        all_games_power += min_red * min_blue * min_green
    return all_games_power


print("-> Part One:", part_one(games))
print("-> Part Two:", part_two(games))
