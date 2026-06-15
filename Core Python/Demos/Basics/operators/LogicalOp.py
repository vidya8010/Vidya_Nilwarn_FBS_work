### and : If both operands are True then return True otherwise False
print(True and False)

### or : If both operands are False then return False otherwise True
print(True or False)

### not : Opposite of operands
print(not True)

#Practice : Check user is eligible for vote or not 
a=13
t=a>=18
message='eligible for vote'*t + 'not eligible'*(not t)
print(message)