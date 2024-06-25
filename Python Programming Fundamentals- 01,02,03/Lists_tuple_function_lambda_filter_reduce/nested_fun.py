"""def f():
    def g():
        print('inside function g')
        f()
    g()
    print('inside function f')
f()"""

"""def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)
"""
# type and id
"""def square(num):
  return num**2

type(square)

id(square)"""

# reassign
"""x = square
id(x)
x(3)
"""


# deleting a function
"""del square
square(3)
"""

# storing
"""L = [1,2,3,4,square]
L[-1](3)"""

#Assignments
"""def hour_to_minute(n):
    minutes = n*60

    return minutes

y = hour_to_minute(4)
print(y)"""

"""def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)"""


"""def f():
    def x(a, b):
        return a + b

    return x


val = f()(3, 4)
print(val)"""

"""def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))"""


"""
Benefits of using a Function
Code Modularity
Code Readibility
Code Reusability
"""