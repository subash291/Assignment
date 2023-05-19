import json

with open(r'C:\Users\subash.s\Downloads\sample_data.json') as f:
    data = json.load(f)
    emp_list = []
    parameters = data['parametersList']
for req_data in parameters:
    req_dict = {
        'parameterName': req_data['parameterName'],
        'min_value': req_data['min'],
        'max_value': req_data['max'],
        'average_value': req_data['avg']
    }
    emp_list.append(req_dict)
    req_list = json.dumps(emp_list, indent=1)
print(req_list)
with open('final_output.json', 'w') as f1:
    f1.write(req_list)
