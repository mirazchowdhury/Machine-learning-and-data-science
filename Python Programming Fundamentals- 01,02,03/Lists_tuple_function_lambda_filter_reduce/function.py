def is_even(num):
    """
    This function returns if the given number is oddd or even
    Input --> Any valid integer
    Output --> Odd/Even

    Created on Thursday,March 14, 2024 at 2.31 am
    """
    if type(num) == int:
        if num%2 == 0:
            return "is even"
        else:
            return "is odd"
    else:
        return "Bolod"

for i in range(1,11):
    x = is_even(i)
    print(x)

print(is_even.__doc__)

