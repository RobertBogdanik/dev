import json
from xml.etree.ElementInclude import include


file = open('./schemat.csv', "r")
Lines = file.readlines()

# jsson = []
print("[")
for line in Lines:
    # print("line")
    subJsson = []
    for part in line.split(','):
        part.replace('\n', '')
        if part=='' or part=='\n':
            subJsson.append(0)
        else:
            subJsson.append(part)
    # subJsson.append(-1)
        
    

    print(json.dumps(subJsson), end=',\n')
    # print(",")
    # jsson.append(subJsson)
    # print(str(subJsson)+",")

print("]")

# print(json.dumps(jsson))