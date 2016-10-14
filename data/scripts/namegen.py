import csv,json

def csv_to_list(path):
    with open(path,'rb') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def rows_to_jsarray (names,arrkey):
    i = 1
    field_names = names[0]
    arr = []
    for name in names[1:]:
        jobj = {}
        for field,i in zip(field_names,range(0,len(field_names))):
            jobj[field] = name[i]
        arr.append(jobj)
    return {arrkey:arr}

def dump_json (path,jsdata):
    with open(path,'wb') as fl:
        fl.write(json.dumps(jsdata))

if __name__ == '__main__':
    path = "..\\csv\\cities.csv"
    jspath = "..\\json\\cities.json"
    cities = csv_to_list(path)
    assert len(cities) == 56
    jsdata = rows_to_jsarray(cities,'cities')
    dump_json(jspath,jsdata)
