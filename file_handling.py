import json 
import csv 
import os 

print(os.path.dirname(__file__))


try:
    with open('input.json', 'r')  as file_object:
        python_object = [json.loads(line) for line in file_object]
        print(python_object, type(python_object))

    with open('output.json', 'w') as file_object:
        json.dump(python_object,file_object)

except FileNotFoundError:
    print('file is not found')