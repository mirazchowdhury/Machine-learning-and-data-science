#Lambda Function
#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

"""a = lambda x:x**2
print(a(2))

c = lambda x,y:x*x+y
print(c(2,3))
"""

"""
Diff between lambda vs Normal Function
No name
lambda has no return value(infact,returns a function)
lambda is written in 1 line
not reusable
"""

"""
Then why use lambda functions?
They are used with HOF
"""

"""a = lambda s:'d' in s
print(a("hello"))"""

"""e = lambda x:'even' if x%2==0 else 'odd'
print(e(121))"""


"""def square(x):
  return x**2

def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)


L = [1,2,3,4,5]

transform(square,L)"""

# Example

"""def square(x):
  return x**2

def cube(x):
  return x**3"""

# HOF
"""def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**3,L)"""