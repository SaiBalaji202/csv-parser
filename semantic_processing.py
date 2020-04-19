from pprint import pprint
from csv import DictWriter, DictReader

with open('./users.csv', 'w') as file:
    header = ('First Name', 'Last Name', 'Age')

    csv_writer = DictWriter(
        file,
        fieldnames=header,
        lineterminator='\n'
    )

    data = (
        {
            'First Name': 'Balaji',
            'Last Name': 'S',
            'Age': 22
        },
        {
            'First Name': 'Gokul',
            'Last Name': 'S',
            'Age': 23
        },
        {
            'First Name': 'Lakshman',
            'Last Name': 'P',
            'Age': 28
        }
    )
    csv_writer.writeheader()

    csv_writer.writerows(data)

with open('./users.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    for row in data:
        pprint(row)
    for row in data:
        pprint(row)
