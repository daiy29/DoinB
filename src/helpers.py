import json

def jsonLoader(filename):

    with open(filename, 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    return obj

def msToTime(ms):
    minutes = ms // 60
    ms %= 60
    if ms < 10:
        return str("%d:0%d" % (minutes, ms))
    else:  
        return str("%d:%d" % (minutes, ms))

