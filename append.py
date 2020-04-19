from csv import DictWriter

with open('./users.csv', 'a') as file:

    csv_writer = DictWriter(
        file,
        fieldnames=('First Name', 'Last Name', 'Age'),
        lineterminator='\n'
    )

    data = [
        {
            'First Name': 'Vijay',
            'Last Name': 'S',
            'Age': 22
        },
        {
            'First Name': 'Raj',
            'Last Name': 'S',
            'Age': 23
        },
    ]

    csv_writer.writerows(data)
