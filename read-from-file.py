import csv
import json

# with open("input01.txt") as f:
#     c = csv.reader(f, delimiter=' ', skipinitialspace=True)
#     for line in c:
#         print(line)

# with open('data.json') as f:
#     data = json.load(f)
#     print(data)

def get_data(path):
    with open(path) as file:
        output = []
        for line in file:
            output.append(json.loads(line.rstrip('\n')))
        return output

print(get_data('input.txt'))
