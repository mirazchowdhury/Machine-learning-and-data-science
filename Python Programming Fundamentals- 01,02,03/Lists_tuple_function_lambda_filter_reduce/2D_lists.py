A = [[1,2,3,4,5],
     [-5,-6,-8,10,11],
     [11,23,33,27,29]]
"""print(A[2][-1]+A[2][2])"""
column = []
for row in A:
    column.append(row[2])

print(column)