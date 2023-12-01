from AdventOfCode2023 import day_01

with open("AdventOfCode2023/SampleData/sample_01_1.txt", "r") as file:
    sample_data_one = [row.strip() for row in file.readlines()]

with open("AdventOfCode2023/SampleData/sample_01_2.txt", "r") as file:
    sample_data_two = [row.strip() for row in file.readlines()]


def test_part_one():
    assert day_01.part_one(sample_data_one) == 142


def test_part_two():
    assert day_01.part_two(sample_data_two) == 281
