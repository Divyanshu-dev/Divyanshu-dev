# # Passing a func as a parameter:
# numbers=[1,2,3,4,5]
# def add_new(numbers, func1):
#     result=[]
#     for i in numbers:
#         result.append(func1(i))
#     return result

# def square(x):
#     return x**2
# calling_fun=add_new(numbers,square)
# print(calling_fun)


def disp(sh):
    print("Disp function"+" " +sh())

def show():
    return "show function"

disp(show)