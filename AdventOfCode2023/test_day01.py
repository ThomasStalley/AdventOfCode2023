from AdventOfCode2023 import day_01

sample_data_one = [row.strip() for row in open("AdventOfCode2023/SampleData/sample_01_1.txt", "r").readlines()]
sample_answer_one = 142
sample_data_two = [row.strip() for row in open("AdventOfCode2023/SampleData/sample_01_2.txt", "r").readlines()]
sample_answer_two = 281


def test_part_one():
    assert day_01.part_one(sample_data_one) == sample_answer_one


def test_part_two():
    assert day_01.part_two(sample_data_two) == sample_answer_two
