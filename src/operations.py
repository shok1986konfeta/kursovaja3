import json


def parse_operations(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    operations = []
    for operation in data['operations.zip']:
        if operation['status'] == 'EXECUTED':
            operations.append({
                'id': operation['id'],
                'date': operation['date'],
                'state': operation['state'],
                'operationAmount': operation['operationAmount'],
                'description': operation['description'],
                'from': operation['from'],
                'to': operation['to'],
            })

    return operations
