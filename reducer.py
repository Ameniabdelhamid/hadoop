#!/usr/bin/python
import sys
import json
from subprocess import Popen, PIPE

output_dict = {}
#holds the accounts records against orgno
accounts_dict = {}


for line in sys.stdin:
    org_number, value = line.strip().split("||")
    input_json = json.loads(value)

    if len(input_json.keys()) == 5:
        output_dict[org_number] = input_json
    else:
        if org_number in accounts_dict:
            accounts_array = list(accounts_dict[org_number])
            accounts_array.append(input_json)
            accounts_dict[org_number] = accounts_array
        else:
            accounts_dict[org_number] = [input_json]


for key in output_dict.keys():
    if key in accounts_dict.keys():
        output_dict[key]['accounts'] = accounts_dict[key]

    output_dict[key] = {k: v for k, v in output_dict[key].items() if v}
    f = open("/home/ameni/Desktop/hadoopJsonPy/output/" + key + ".json", "w+")
    f.write(str(json.dumps(output_dict[key])))
    #cat = Popen(["hadoop", "fs", "-ls", "/pythontuto/OutputJson/outputss"], stdout=PIPE)    
    #put = Popen(["hadoop", "fs", "-put", "/home/ameni/Desktop/hadoopJsonPy/output/"+key+".json", "/pythontuto/OutputJson/outputss/"],stdin=cat.stdout)
    f.close()
    #put.communicate()
  

