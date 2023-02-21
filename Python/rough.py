numbers = [3, 5]

sum_init=0

for num in numbers:
    sum_init=sum_init + num **2
print("The sum of squares is: ", sum_init)




def add_new(number,func):
    result=[]
    for i in number:
        result.append(func(i))
    return result


def add(x):
    return x**2

number=[1,2,3,4,5]
calldFunc=add_new(number,add)
print(calldFunc)