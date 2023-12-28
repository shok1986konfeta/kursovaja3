import datetime
import json
from typing import Any, Dict, List
import os


def getting_data_from_file() -> Any:
    """ считывает из файла данные """
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, 'data', 'operations.json')
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def filtering_sorting_list(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """ Принимает список данных и выводит только проведенные 5 последние операции в виде списка словарей"""
    list_to_be_sorted = (item for item in data if item.get('state') == 'EXECUTED')
    last_operation = sorted(list_to_be_sorted, key=lambda d: d['date'])[-5:]
    return sorted(last_operation, key=lambda d: d['date'], reverse=True)


def card_number(number_card: Any) -> Any:
    """ Функция принимает строку, вычисляет по длине номер или счет и выводит замаскированный тип и номер """
    num = "".join(n for n in number_card if n.isdecimal())
    type_num = "".join(s for s in number_card if s.isalpha())
    if len(num) == 16:
        return f"{type_num} {num[0:4]} {num[4:6]}** **** {num[12:17]}"
    if len(num) == 20:
        return f"{type_num} **{num[16:21]}"


def date_converter(str_date: str) -> Any:
    """ Функция принимает строку и выдает дату в формате %d-%m-%Y """
    date_time_str = str_date[:10]
    return datetime.datetime.strptime(date_time_str, '%Y-%m-%d').strftime('%d-%m-%Y')