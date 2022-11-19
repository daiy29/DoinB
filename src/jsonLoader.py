import json

def jsonLoader(filename):

    with open(filename, 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    return obj