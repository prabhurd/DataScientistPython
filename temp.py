def log(func):
    def inner(*args,**kwargs):
        print(f'Enter function : {str(func).replace("<","").split(" ")[1]}()')
        func(*args,**kwargs)
        print(f'Exit function : {str(func).replace("<", "").split(" ")[1]}()')
    return inner

def check(func):
    def inside(a,b):
        if b==0:
            print("Cannot Divide By Zero")
            return
        return func(a,b)
    return inside

@log
def div(a,b):
    return a/b

num = div(10,5)
print(num)


#



@log
def tet(firstname,lastname):
    print(firstname,lastname)

tet("Prabhu","Rd")