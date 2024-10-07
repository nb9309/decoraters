def lower(as_upper):
    def convert_lower():
        x,y = as_upper()
        z = x.lower()
        return x,y,z
    return convert_lower

def upper(as_text):
    def convert_upper():
        x = as_text()
        z = x.upper()
        return x,z
    return convert_upper

def text():
    return input('enter text: ').capitalize()

x,y,z = lower(upper(text))()

print(f' {x}\n {y}\n {z}\n')