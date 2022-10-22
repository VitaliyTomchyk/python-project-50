#test file for generate_difference.py
from gendiff.scripts.gendiff_script import generate_diff


def test_generate_diff_json():
    file = open('./tests/fixtures/results/fixture_gendiff_test.txt', 'r')
    result = file.read()
    assert generate_diff('tests/fixtures/JSON/file1.json',
                         'tests/fixtures/JSON/file2.json') == str(result)


test_generate_diff_json()


def test_generate_diff_json_2():
    file = open('./tests/fixtures/results/fixture_gendiff_test_2.txt', 'r')
    result = file.read()
    assert generate_diff('tests/fixtures/JSON/file1_2.json',
                         'tests/fixtures/JSON/file2_2.json') == str(result)


test_generate_diff_json_2()


def test_generate_diff_json_plain():
    file = open('./tests/fixtures/results/fixture_gendiff_test_3.txt', 'r')
    result = file.read()
    assert generate_diff('tests/fixtures/JSON/file1_2.json',
                         'tests/fixtures/JSON/file2_2.json',
                         format='plain') == str(result)


test_generate_diff_json_plain()


def test_generate_diff_yaml():
    file = open('./tests/fixtures/results/fixture_gendiff_test.txt', 'r')
    result = file.read()
    assert generate_diff('tests/fixtures/YML/file1.yml',
                         'tests/fixtures/YML/file2.yml') == str(result)


test_generate_diff_yaml()


def test_generate_diff_yaml_1():
    file = open('./tests/fixtures/results/fixture_gendiff_test_2.txt', 'r')
    result = file.read()
    assert generate_diff('tests/fixtures/YML/file1_2.yml',
                         'tests/fixtures/YML/file2_2.yml') == str(result)


test_generate_diff_yaml_1()
