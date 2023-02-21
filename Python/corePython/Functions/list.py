#list in a python is a data structure which stores heterogenious objects 
#it is mutable in nature so that we can change the values.
# the size is dynamic.
#empty list = []


list1=[1,2222,3,4,5]
# for i in list1:
#     result=i+1
#     print(result)


#accessing via index number.
p=len(list1)
print(p)

# for i in range(p):
#     print(i,list1[i])

# list1.count(1)
# print("asxaq", list1)



#use of map and filter in list:

#filter the list having >60

list2=[10,30,90,30,51,99,77,66]
def more_than_sixty(n):
    if n>=60:
        return True

r=map(more_than_sixty,list2)
print(r)


