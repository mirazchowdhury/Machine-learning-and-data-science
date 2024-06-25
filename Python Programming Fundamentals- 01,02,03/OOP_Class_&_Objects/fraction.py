class Fraction:
    def __init__(self,x,y):
        self.den=x
        self.num=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self, other):
        new_num = self.den*other.num+other.den*self.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)

    def __sub__(self, other):
        new_num = other.den * self.num - self.den * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num, new_den)

    def convert_to_decimal(self):
        return self.num/self.den


obj1 = Fraction(6,7)
obj2 = Fraction(6,7)


print(obj1.convert_to_decimal())
print(obj2)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
print(type(Fraction))
