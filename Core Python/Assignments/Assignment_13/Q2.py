#2. Python Program to Concatenate Two Dictionaries Into One
def cancatDict(d1,d2):
    d1.update(d2)
    return d1
d1={1:'a',2:'b',3:'c'}
d2={4:'d',5:'e'}
print(cancatDict(d1,d2))