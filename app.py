# Link to the Tutorial Video - https://youtu.be/Sul7LtaIKnw

# 1) Creating CSV file
# 2) Adding row
# 3) Adding Multiple Rows
# 4) Reading Rows
# 5) 2nd Approach
#     i) Reading
#     ii) Writing
# 6) Append New Rows at the end of the file
# 7) Updating (update cell, column, row)
# 8) Deleting (column, row, cell)

from csv import writer, reader

# with open('./users.csv', 'w') as file:
#     csv_writer = writer(file, lineterminator='\n')
#     header = ('First Name', 'Last Name', 'Age')
#     data = (
#         ('Balaji', 'S', 22),
#         ('Gokul', 'S', 23),
#         ('Lakshman', 'P', 28)
#     )

#     csv_writer.writerow(header)
#     csv_writer.writerows(data)

with open('./users.csv') as file:
    csv_reader = reader(file, delimiter='\t')
    data = list(csv_reader)
    for row in data:
        print(row)
    for row in data:
        print(row)
