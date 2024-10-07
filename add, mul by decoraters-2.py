def mul(as_add):
    def cals():
        x,y,z = as_add()
        mul = x*y
        return x,y,z,mul
    return cals
def add(as_num):
    def cal():
        x,y = as_num()
        add = x+y
        return x,y,add
    return cal

@mul
@add
def num():
    return int(input('enter value: ')),int(input('enter value: '))

x,y,z,m = num()

print('{}+{}={}, {}*{}={}'.format(x,y,z,x,y,m))