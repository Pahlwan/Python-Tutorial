# dict1={(1,2):3}
# print(dict1[(1,2)])

# dict2={1:"mukesh",(2,3):"Padma","maneesh":5}
# print(dict2)

# # for i,value in enumerate(dict2):
#     # print(str(i)+""+map(str,value))


# list1=["1","2","3","4"]

# list2=list(map(int,list1))
# print(list2)

# dict1={1:True,3:"Mukesh",5:False}
# print(all(dict1.values()))

# del dict1[3]
# # dict1.clear()
# print(dict1)
# # del dict1

# print(dict1.get(1,0))
# print(dict1.get(10,"Fuck You"))

# if dict1:
#     print(dict1)

list1=[1,1,1,2,1,2,1,2,2,3,2,3,4,1,1]
dict1={}

for i in list1:
    dict1[i]=dict1.get(i,0)+1

print(dict1)



