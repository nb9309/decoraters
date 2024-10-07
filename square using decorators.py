
def sq(hyd):
    def square():
        x = hyd()
        squar = x**2
        return x,squar
    return square


@sq
def num ():
    return float(input('enter value: '))

x,y = num()
print(type(num))
print(type(sq))
print('square of {} = {}'.format(x,y))