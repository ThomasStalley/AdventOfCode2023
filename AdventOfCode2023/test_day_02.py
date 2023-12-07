from AdventOfCode2023 import day_02

sample_data_one = [row.strip() for row in open("AdventOfCode2023/SampleData/sample_02_1.txt", "r").readlines()]
sample_answer_one = 8

sample_data_two = [row.strip() for row in open("AdventOfCode2023/SampleData/sample_02_2.txt", "r").readlines()]
sample_answer_two = 2286


def test_part_one():
    assert day_02.part_one(sample_data_one) == sample_answer_one


def test_part_two():
    assert day_02.part_two(sample_data_two) == sample_answer_two
