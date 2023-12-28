import json
import pytest
import os
from src.functions import card_number, date_converter, filtering_sorting_list
import unittest


class TestGettingDataFromFile(unittest.TestCase):
    def test_getting_data_from_file(self):
        test_data = {'key1': 'value1', 'key2': 'value2'}
        with open('test_operations.json', 'w', encoding='utf-8') as file:
            json.dump(test_data, file)
        os.remove('test_operations.json')


@pytest.mark.parametrize("test_input, expected", [([
            {'id': 1, 'state': 'PENDING', 'date': '2022-01-01'},
            {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-02'},
            {'id': 3, 'state': 'EXECUTED', 'date': '2022-01-03'},
            {'id': 4, 'state': 'EXECUTED', 'date': '2022-01-04'},
            {'id': 5, 'state': 'EXECUTED', 'date': '2022-01-05'},
            {'id': 6, 'state': 'EXECUTED', 'date': '2022-01-06'},
            {'id': 7, 'state': 'PENDING', 'date': '2022-01-07'},
        ], [
            {'id': 6, 'state': 'EXECUTED', 'date': '2022-01-06'},
            {'id': 5, 'state': 'EXECUTED', 'date': '2022-01-05'},
            {'id': 4, 'state': 'EXECUTED', 'date': '2022-01-04'},
            {'id': 3, 'state': 'EXECUTED', 'date': '2022-01-03'},
            {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-02'},
        ])])
def test_filtering_sorting_list(test_input, expected):
    assert filtering_sorting_list([]) == []
    assert filtering_sorting_list(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("VISA 1234 5678 9012 3456", "VISA 1234 56** **** 3456"),
                                                 ("счет 12345678901234567890", "счет **7890")])
def test_card_number(test_input, expected):
    assert card_number(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("2019-08-26T10:50:58.294041", '26-08-2019')])
def test_date_converter(test_input, expected):
    assert date_converter(test_input) == expected