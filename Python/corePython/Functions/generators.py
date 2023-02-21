def simplegenfunc():
    yield 1
    yield 2
    yield 3
    yield 4

x=simplegenfunc()
    # print(x)
print(next(x))
print(next(x))
print(next(x))


#fibnocci series using generator

# 011235813

def fbon(limit):
    a,b=0,1
    while a<limit:
        print("\nUsing loop")
        yield a
        a,b=b,a+b
x=fbon(5)
print("\nUsing for in loop")
for i in fbon(5):
    print(i)






