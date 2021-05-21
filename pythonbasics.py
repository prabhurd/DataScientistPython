x = 8
print(callable(x))

def sum(a,b):
    pass

print(callable(sum))


string = "Hello World."
array = bytes(string, 'utf-8')
print(array)

string = "Hello World."
array = bytes(string, 'utf-16')
print(array)

# compile string source to code
code_str = 'x=5\ny=10\nprint("sum =",x+y)'
code = compile(code_str, 'sum.py', 'exec')
print(type(code))
exec(code)
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(otherText)
print(ascii(otherText))

print('Pyth\xf6n is interesting')