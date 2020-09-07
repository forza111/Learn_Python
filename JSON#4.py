import json
data = {
    'president':{
        'name': 'Pytin',
        'special': 'Volodka'
    }
}




with open('data_file.json','w') as write_file:
    json.dump(data, write_file,indent = 4)

