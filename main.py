from ast import main
from src import mask
from src import operations
import datetime
import zipfile
import json


def parse_operations():
    with zipfile.ZipFile('operations.zip') as zip_file:
        with zipfile.open('operations.zip.json') as f:
            data = json.load(f)
    return data


operations = parse_operations()

for i in range(5):

    for operation in operations:
        if operation['id'] is None:
            raise ValueError('Недопустимая запись: {}'.format(operation))

    for operation in operations[:5]:
        date = datetime.datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        date = date.strftime('%d.%m.%Y')
        print('{} {} {} -> {} {} {}'.format(
            date, operation['description'],
            mask.mask_card_number(operation['from']),
            mask.mask_account_number(operation['to']),
            operation['operationAmount']['amount'],
            operation['operationAmount']['currency']))

if name == '__main__':
    main()