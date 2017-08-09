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
import collections
# for key in d:
#     print(key)
#
# for key in d.keys():
#     print(key, "->", d[key])
#
# for value in d.values():
#     print(value)


# student1 = {"name":'Alise', "age": 24, "year": 2, "grant": 1000, "bonus": 1000}
# student2 = {"name":'Bob', "age": 22, "year": 1}
# student3 = {"name":'Bill', "age": 25, "year": 3}
#
# group = [student1,student2, student3]
# for student in group:
#     if "grant" in student:
#         student["grant"] += 500
#     else :
#         student["grant"] = 1000

#
# pprint.pprint(group)

# group.sort(key=lambda student: student ["grant"])
# # pprint.pprint(group)
# # print()
#
# group.sort(key=lambda student: (student ["grant"], student ["name"]), reverse=True )
# pprint.pprint(group)
# print()
# print (student1)

d = collections.OrderedDict()
d["age"] = 42
d["name"] = "Bill"
d["title"] = "CEO"
d["dep"] = "IT"
d["salary"] = 4200
d["bonus"] = 4000

print (d)

def print_entry(entry):

    # for key in entry:
    #     print ("%s:\t%s" % (key, entry[key]))
    for key, value  in entry. items():
        print("%s:\t%s" % (key, value)

print_entry(d)

print



