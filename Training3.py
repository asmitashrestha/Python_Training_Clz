# a= 2
# b=a**2
# print(b)
# result_list = []
# my_list = [1,2,3,4]
# for i in my_list:
    # if(i % 2 == 0):

    #     # print("New list ", i**2)
    #     result_list.append(i**2)
    #     print("New list",result_list)
    # else:
    #     result_list.append(i)
    #     print("new list",result_list)
    #     # print("New list", i)  


# my_list =[i**2 for i in my_list if(i % 2 == 0)]
# print("list",my_list)


# my_string =""""
# sjhdgskhc hch\"g xouchuocbs sbwjkeuwcsdjkchwjkj bsdjbvsdbvsdjsd
# """
# print(my_string)

# myString = "This is the python training in sagarmatha college"

# print(myString.replace("T","a"))

# print(myString.replace("sagarmatha college","everest campus"))
# print(myString.title())
# print(myString.capitalize().replace("T","p"))

# print(myString.upper())
# print(myString.capitalize())


# lists ="        hello it's me "
# print(lists.lstrip())
# print(lists.rstrip("me"))

name_string =["asmita","arjun"]
name = "asmita"
address = ["thankot","kalanki"]
# mystr = f"My name is {name} .I live in {address}."
# print(mystr)

mystring = ["my name is {0}".format(name,address ) for name in name_string]
delimeter = "..."

res_string = delimeter.join(mystring)
print(res_string)


