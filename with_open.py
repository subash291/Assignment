import json

with open('datas.json', 'r') as file:
    data = json.load(file)
name = data['name']
college = data['college']
company = data['company']

print(name)
print(college)
print(company)