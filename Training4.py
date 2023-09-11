dictionaries = {
    "name":"Asmita",
    "address":"gujudhara",
    "faculty":"CSIT"
}
dictionaries["contact"]=980989789

dictionaries["name"] = "sakina"

print(dictionaries)
# print(dictionaries["name"])

for key,value in dictionaries.items():
    print(key,value)

dictionariestwo = {
    "college" :"sagarmatha",
    "location":"sanepa",
    "faculty":["csit","bca","engineering"],
    "addvalue":dictionaries
}
print(dictionariestwo)


oddeven ={}
odd_even_check = {
    "va1":1,
    "va2":2,
    "va3":3,
    "va4":4,
    "va5":5,
    "va6":6
}

# even_dict = {key:value for key,value in odd_even_check.items() if value%2==0 }
# print(even_dict)

# for key, value in odd_even_check.items():
#     if(value%2==0):
#         print("even",key,value)

def evencheck(random_dict):
    result_dict ={key:value for key,value in random_dict.items() if value%2==0}
    return result_dict

print(evencheck(odd_even_check))


a=[1,2,3,4,5] # shallow copy of the dictionary
b=a.copy()
a.pop()
print(a)
print(b)

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

ref_list =old_list.copy()
old_list.pop()
print("ref list",ref_list)
print("Old list:", old_list)
print("New list:", new_list)




