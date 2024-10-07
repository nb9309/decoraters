def vals():
    return int(input()),int(input())

def add(alias):
    def cal():
        x,y=alias()
        z = x+y
        return x,y,z
    return cal()


x,y,z = add(vals)
print('{}+{}={}'.format(x,y,z))