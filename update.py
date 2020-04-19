from csv import DictReader, DictWriter
from tempfile import NamedTemporaryFile
import shutil

with open('./users.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)

with NamedTemporaryFile(mode='w', delete=False) as temp_file:
    header = ('Name', 'Age')

    csv_writer = DictWriter(
        temp_file,
        fieldnames=header,
        lineterminator='\n'
    )
    csv_writer.writeheader()
    for row in data:
        if row['Name'] == 'Gokul S':
            continue
        csv_writer.writerow(row)

    print(temp_file.name)


shutil.move(temp_file.name, './users.csv')
