d = {"earth":"земля", "mars":"марс", "venus":"венера"}
d["mercury"] = "меркурий"

# if "earth" in d:
#     print (" found earth")
#     del d["earth"]
# else:
#     print (" Not found")
#
# if "марс" in d.values():
#     print (" found mars")
#     del d["mars"]
# else:
#     print (" Not found")

d["venus"] = "Венера"


# print (d)
#
# country = {"Ukraine":"Kyiv", "Germany":"Berlin", "USA":"Washinton", "Canada":"Toronto"}
# print (country["Canada"])
#
# product = {"Apple": ["iPad","iPod","iPhone","iBook"]}
# print(product)
# product["Apple"].append('iWatch')
# print(product)

import pprint
for key in d:
    print(key)

for key in d.keys():
    print(key, "->", d[key])

for value in d.values():
    print(value)


student1 = {"name":'Alise', "age": 24, "year": 2, "grant": 1000}
student2 = {"name":'Bob', "age": 22, "year": 1}
student3 = {"name":'Bill', "age": 25, "year": 3}

group = [student1,student2, student3]
for student in group:
    if "grant" in student:
        student["grant"] += 500
    else :
        student["grant"] = 1000


pprint.pprint(group)