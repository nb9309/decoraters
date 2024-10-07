
def mul (as_add):
    def calculation():
        x,y,add = as_add()
        m = x*y
        return x,y,m,add
    return calculation

def add(as_num):
    def cal():
        x,y=as_num()
        add = x+y
        return x,y,add
    return cal

def num():
    return int(input('enter first value: ')),int(input('enter second value: '))

x,y,m,z= mul(add(num))()

print('{}+{}={}, {}*{}={}'.format(x,y,z,x,y,m))