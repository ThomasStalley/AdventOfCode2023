import numpy as np
from math import prod

input_content = open("AdventOfCode2023/InputData/input_03.txt", "r").readlines()


class Grid:
    def __init__(self, grid_txt: list[str]):
        self.grid = np.array([[ele for ele in row.strip()] for row in grid_txt])
        self.size = self.grid.shape[0]
        self.records = self.get_records()

    def __iter__(self):
        for i, row in enumerate(self.grid):
            for j, element in enumerate(row):
                yield (i, j), element

    def __getitem__(self, point):
        i, j = point
        return self.grid[i, j]

    def __setitem__(self, point, value):
        i, j = point
        self.grid[i, j] = value

    def get_records(self):
        records = {}
        coordinates_covered = set()
        for point, element in self:
            i, j = point
            if (point in coordinates_covered) or (not element.isdigit()):
                continue

            # Found first element in a potentially longer number:
            current_number = element
            coordinate_keys = [f"{i}_{j}"]
            coordinates_covered.add((i, j))

            # Check if number is longer than the one digit we have found:
            search_index = 1
            while (j + search_index) < self.size and self[i, j + search_index].isdigit():
                current_number += self[i, j + search_index]
                coordinate_keys.append(f"{i}_{j + search_index}")
                coordinates_covered.add((i, j + search_index))
                search_index += 1

            # Add found number to records:
            for key in coordinate_keys:
                records[key] = {"number": int(current_number), "coordinate_keys": coordinate_keys}
        return records


def _get_surrounding_coordinates(coordinates, grid_size):
    surrounding = set()
    for (i, j) in coordinates:
        for surrounding_i in range(-1, 2):
            for surrounding_j in range(-1, 2):
                new_i, new_j = i + surrounding_i, j + surrounding_j

                # Add new coordinate to surrounding coordinate set, if new coordinate is within the overall grid:
                surrounding.add((new_i, new_j)) if (0 <= new_i < grid_size) and (0 <= new_j < grid_size) else None
    return surrounding


def _get_surrounding_characters(grid, surrounding_coordinates):
    return [grid[i, j] for (i, j) in surrounding_coordinates]


def _check_surrounding_characters(surrounding_characters):
    return any(symbol in ["#", "£", "*", "&", "%", "$", "-", "@", "+", "=", "/"] for symbol in surrounding_characters)


def part_one(input_list):
    sum_of_numbers = 0
    schematic_grid = Grid(input_list)
    schematic_grid_size = schematic_grid.size

    coordinates_covered = set()
    for point, element in schematic_grid:
        i, j = point
        if (point in coordinates_covered) or (not element.isdigit()):
            continue

        # Found first element in a potentially longer number:
        current_number = element
        coordinate_keys = [f"{i}_{j}"]
        current_coordinates = [(i, j)]
        coordinates_covered.add((i, j))

        # Check if number is longer than the one digit we have found:
        search_index = 1
        while (j + search_index) < schematic_grid_size and schematic_grid[i, j + search_index].isdigit():
            current_number += schematic_grid[i, j + search_index]
            coordinate_keys.append(f"{i}_{j + search_index}")
            current_coordinates.append((i, j + search_index))
            coordinates_covered.add((i, j + search_index))
            search_index += 1

        surrounding_coordinates = _get_surrounding_coordinates(current_coordinates, schematic_grid_size)
        surrounding_characters = _get_surrounding_characters(schematic_grid, surrounding_coordinates)
        surrounding_characters_contains_symbol = _check_surrounding_characters(surrounding_characters)
        if surrounding_characters_contains_symbol:
            sum_of_numbers += int(current_number)
    return sum_of_numbers


def part_two(input_list):
    sum_of_gear_ratios = 0
    schematic_grid = Grid(input_list)
    schematic_grid_size = schematic_grid.size
    records = schematic_grid.records

    for point, element in schematic_grid:
        if element != "*":
            continue
        current_coordinates = [point]
        surrounding_coordinates = _get_surrounding_coordinates(current_coordinates, schematic_grid_size)
        surrounding_keys = [f"{row}_{col}" for row, col in surrounding_coordinates]

        numbers_found = []
        keys_found = set()
        for key in surrounding_keys:
            number_container = records.get(key)
            if number_container and (key not in keys_found):
                numbers_found.append(number_container.get("number"))
                coord_keys = number_container.get("coordinate_keys")
                keys_found.update(coord_keys) if isinstance(coord_keys, list) else keys_found.add(coord_keys)

        if len(numbers_found) == 2:
            sum_of_gear_ratios += prod(numbers_found)
    return sum_of_gear_ratios


print("-> Part One:", part_one(input_content))
print("-> Part Two:", part_two(input_content))
