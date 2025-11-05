print(
    '''
    ************************
    * Generators in Python *
    ************************
    '''
)
def fun():
    yield 1
    yield 2
    yield 3

for x in fun():
    print(x)
print("\n")
def count_up(n):
    count=1
    while count<=n:
        yield count
        count+=1
a=int(input("Enter the Numbers to count : "))
for x in count_up(a):
    print(x)
print("\n")
print("Large Sequence...")
def larges(n):
    for i in range(n):
        yield i

gen=larges(1000)
print(next(gen))
print(next(gen))
print(next(gen))
print("\n")
print("Simple Generators...")
def simple_gen():
    yield "George"
    yield "John"
    yield "Edwin"

ds=simple_gen()
print(next(ds))
print(next(ds))
print(next(ds))
print("\n")
print("Generators Expression.....")
list1=[x*x for x in range(5)]
print(list1)
genlist=(x*x for x in range(5))
print(genlist)
print(list(genlist))
print("\n")
print("Summing the Squares....")
total =sum(x *x for x in range(5))
print(total)
print(
    '''
    ***************************
    * Fibonacci in Generators *
    ***************************
    '''
)
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

gen=fibonacci()
for _ in range(100):
    print(next(gen))
print("\n")
print(
    '''
    *********************
    * Generator Methods *
    *********************
    '''
)
print("Echo Generator...")
def echo_generator():
    while True:
        rec=yield
        print("Received : ",rec)
gen=echo_generator()
next(gen)
gen.send("Hello")
gen.send("World!!!")
print("\n")
print("using close function.......")
def gene():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator Closed....")
gen=gene()
print(next(gen))
gen.close()
