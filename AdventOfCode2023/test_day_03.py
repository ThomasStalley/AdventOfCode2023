from AdventOfCode2023 import day_03

sample_data_one = [
    [ele for ele in row.strip()] for row in open("AdventOfCode2023/SampleData/sample_03_1.txt", "r").readlines()
]
sample_answer_one = 4361

sample_data_two = [
    [ele for ele in row.strip()] for row in open("AdventOfCode2023/SampleData/sample_03_2.txt", "r").readlines()
]
sample_answer_two = 467835


def test_part_one():
    assert day_03.part_one(sample_data_one) == sample_answer_one


def test_part_two():
    assert day_03.part_two(sample_data_two) == sample_answer_two
