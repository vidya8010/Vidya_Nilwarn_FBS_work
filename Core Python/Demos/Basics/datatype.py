###Numeric category
#integer
x=10
print(type(x))
#float
x=3.14
print(type(x))
#complex
x=10+1j
print(type(x))

###text category
#str
#single line
x='vidya'
print(type(x))
#dougle quotes
x="vidya"
print(type(x))
#triple quotes
x='''vidya'''
print(type(x))


#in most of documentation we use triple quotes for documentation purpose but those are executatble part. dont use it as comment
#Also python does not have any type of multi line comments



###Sequential category

#list
x=[10,20,30]

#tuple
x=(10,20,30)

#range
x=range(1,10)

###set type
#1.set 
x={1,2,3,4,5}

#2 frozen set
x=frozenset({1,2,3,4,5})

###Mapping type
#1.dictionary
x={
    1:'python',
    2:'java'
}
print(x[1])


####Others

#1.Boolean

x=True
print(type(x))

#2. None
x=None
print(type(x))