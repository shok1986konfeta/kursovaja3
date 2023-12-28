from src.functions import card_number, date_converter, filtering_sorting_list, getting_data_from_file

list_operations = getting_data_from_file()
operations = filtering_sorting_list(list_operations)

for operation in operations:
    if operation['description'] == 'Открытие вклада':
        print(f'''{date_converter(operation['date'])} {operation['description']}
Неизвестно -> {card_number(operation['to'])}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}
''')
    else:
        print(f'''{date_converter(operation['date'])} {operation['description']}
{card_number(operation.get('from'))} -> {card_number(operation['to'])}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}
''')