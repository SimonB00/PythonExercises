import json
from collections import Counter

with open('birthdays.json') as f:
    birthdays = json.load(f)

months_count = {'January': 0, 'February' : 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 
'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

for name in birthdays:
    date = birthdays[name].split(sep='-')
    if(date[1] == '01'):
        months_count['January'] += 1
    if(date[1] == '02'):
        months_count['February'] += 1
    if(date[1] == '03'):
        months_count['March'] += 1
    if(date[1] == '04'):
        months_count['April'] += 1
    if(date[1] == '05'):
        months_count['May'] += 1
    if(date[1] == '06'):
        months_count['June'] += 1
    if(date[1] == '07'):
        months_count['July'] += 1
    if(date[1] == '08'):
        months_count['August'] += 1
    if(date[1] == '09'):
        months_count['September'] += 1
    if(date[1] == '10'):
        months_count['October'] += 1
    if(date[1] == '11'):
        months_count['November'] += 1
    if(date[1] == '12'):
        months_count['December'] += 1

months = []
for name in birthdays:
    date = birthdays[name].split(sep='-')
    months.append(date[1])
counter = Counter(months)
print(counter)
print(months_count)