import json

birthdays = {
    'Simone': '04-12-2000',
    'Alessandro': '21-05-2000',
    'Niccolò': '07-05-2000'
}

with open('birthdays.json','w') as f:
    json.dump(birthdays, f)