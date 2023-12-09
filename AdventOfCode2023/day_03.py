import numpy as np

with open("AdventOfCode2023/InputData/input_03.txt", "r") as file:
    schematic_input = [[ele for ele in row.strip()] for row in file.readlines()]


def _get_surrounding_coordinates(i, j, number_size, grid_size):
    # Define the range of cells based on the type
    if number_size == 'single':
        coordinates = [(i, j)]
    elif number_size == 'double':
        coordinates = [(i, j), (i, j + 1)]
    elif number_size == 'triple':
        coordinates = [(i, j), (i, j + 1), (i, j + 2)]
    else:
        return

    surrounding = set()
    for coordinate in coordinates:
        coordinate_i, coordinate_j = coordinate
        for surrounding_i in range(-1, 2):
            for surrounding_j in range(-1, 2):
                new_i, new_j = coordinate_i + surrounding_i, coordinate_j + surrounding_j

                # Check is surrounding cell is within grid:

                if (0 <= new_i < grid_size) and (0 <= new_j < grid_size):
                    surrounding.add((new_i, new_j))
    return surrounding


def _get_surrounding_characters(grid, surrounding_coordinates):
    surrounding_characters = []
    for coordinate in surrounding_coordinates:
        i, j = coordinate
        character = grid[i, j]
        surrounding_characters.append(character)
    return surrounding_characters


def _check_surrounding_characters(surrounding_characters):
    symbols = ["#", "£", "*", "&", "%", "$", "-", "@", "+", "=", "/"]

    for char in surrounding_characters:
        if any(symbol in char for symbol in symbols):
            return True
    return False


def _get_records(grid):
    records = {}

    for i, row in enumerate(grid):
        for j, ele in enumerate(row):
            next_ele = grid[i, j + 1] if (j + 1) < grid.shape[0] else "."
            next_next_ele = grid[i, j + 2] if (j + 2) < grid.shape[0] else "."

            # One-digit number:
            if ele.isdigit() and (not next_ele.isdigit()):
                current_number = int(f"{ele}")
                coordinates = [f"{i}_{j}"]
                records[f"{i}_{j}"] = {"number": current_number, "coordinates": coordinates}

                # Write out the number, avoid duplicates:
                grid[i, j] = "X"

            # Two-digit number:
            elif ele.isdigit() and next_ele.isdigit() and (not next_next_ele.isdigit()):
                current_number = int(f"{ele}{next_ele}")
                coordinates = [f"{i}_{j}", f"{i}_{j + 1}"]
                records[f"{i}_{j}"] = {"number": current_number, "coordinates": coordinates}
                records[f"{i}_{j + 1}"] = {"number": current_number, "coordinates": coordinates}

                # Write out the number, avoid duplicates:
                grid[i, j] = "X"
                grid[i, j + 1] = "X"

            # Three-digit number:
            elif ele.isdigit() and next_ele.isdigit() and next_next_ele.isdigit():
                current_number = int(f"{ele}{next_ele}{next_next_ele}")
                coordinates = [f"{i}_{j}", f"{i}_{j + 1}", f"{i}_{j + 2}"]
                records[f"{i}_{j}"] = {"number": current_number, "coordinates": coordinates}
                records[f"{i}_{j + 1}"] = {"number": current_number, "coordinates": coordinates}
                records[f"{i}_{j + 2}"] = {"number": current_number, "coordinates": coordinates}

                # Write out the number, avoid duplicates:
                grid[i, j] = "X"
                grid[i, j + 1] = "X"
                grid[i, j + 2] = "X"
    return records


def _multiply_all_elements(input_list):
    product = 1
    for i in input_list:
        product = product * i
    return product


def part_one(input_list):
    sum_of_numbers = 0

    schematic_grid = np.array(input_list)
    grid_size = schematic_grid.shape[0]

    for i, row in enumerate(schematic_grid):
        for j, ele in enumerate(row):
            next_ele = schematic_grid[i, j + 1] if (j + 1) < grid_size else "."
            next_next_ele = schematic_grid[i, j + 2] if (j + 2) < grid_size else "."

            # One-digit number:
            if ele.isdigit() and (not next_ele.isdigit()):
                current_number = int(f"{ele}")
                surrounding_coordinates = _get_surrounding_coordinates(i, j, "single", grid_size)
                surrounding_characters = _get_surrounding_characters(schematic_grid, surrounding_coordinates)
                surrounding_characters_contains_symbol = _check_surrounding_characters(surrounding_characters)
                if surrounding_characters_contains_symbol:
                    sum_of_numbers += current_number

                # Write out the number, avoid duplicates:
                schematic_grid[i, j] = "X"

            # Two-digit number:
            elif ele.isdigit() and next_ele.isdigit() and (not next_next_ele.isdigit()):
                current_number = int(f"{ele}{next_ele}")
                surrounding_coordinates = _get_surrounding_coordinates(i, j, "double", grid_size)
                surrounding_characters = _get_surrounding_characters(schematic_grid, surrounding_coordinates)
                surrounding_characters_contains_symbol = _check_surrounding_characters(surrounding_characters)
                if surrounding_characters_contains_symbol:
                    sum_of_numbers += current_number

                # Write out the number, avoid duplicates:
                schematic_grid[i, j] = "X"
                schematic_grid[i, j + 1] = "X"

            # Three-digit number:
            elif ele.isdigit() and next_ele.isdigit() and next_next_ele.isdigit():
                current_number = int(f"{ele}{next_ele}{next_next_ele}")
                surrounding_coordinates = _get_surrounding_coordinates(i, j, "triple", grid_size)
                surrounding_characters = _get_surrounding_characters(schematic_grid, surrounding_coordinates)
                surrounding_characters_contains_symbol = _check_surrounding_characters(surrounding_characters)
                if surrounding_characters_contains_symbol:
                    sum_of_numbers += current_number

                # Write out the number, avoid duplicates:
                schematic_grid[i, j] = "X"
                schematic_grid[i, j + 1] = "X"
                schematic_grid[i, j + 2] = "X"
    return sum_of_numbers


def part_two(input_list):
    sum_of_gear_ratios = 0
    schematic_grid = np.array(input_list)
    grid_size = schematic_grid.shape[0]
    records = _get_records(schematic_grid)

    for i, row in enumerate(schematic_grid):
        for j, ele in enumerate(row):
            if ele != "*":
                continue
            surrounding_coordinates = _get_surrounding_coordinates(i, j, "single", grid_size)
            surrounding_keys = [f"{row}_{col}" for row, col in surrounding_coordinates]

            numbers_found = []
            keys_found = []
            for key in surrounding_keys:
                number_container = records.get(key)
                if not number_container:
                    continue
                if key in keys_found:
                    continue


                numbers_found.append(records.get(key).get("number"))
                [keys_found.append(coordinate) for coordinate in records.get(key).get("coordinates")]

            if len(numbers_found) == 2:
                sum_of_gear_ratios += _multiply_all_elements(numbers_found)
    return sum_of_gear_ratios


print("-> Part One:", part_one(schematic_input))
print("-> Part Two:", part_two(schematic_input))
