"""a = list(map(lambda x:x**3,[1,2,3,4,5]))
print(a)"""

"""# odd/even labelling of list items
L = [1,2,3,4,5]
a = list(map(lambda x:'even' if x%2 == 0 else 'odd',L))
print(a)"""

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

a = list(map(lambda users:users['gender'],users))
print(a)