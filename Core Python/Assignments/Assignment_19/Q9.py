# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def my_range(start,stop,step):
    if step==0:
        raise ValueError("step cannot be zero")
    if step>0:
        while start<stop:
            yield start
            start+=step
    else:
        while start>stop:
            yield start
            start+=step
for i in my_range(10, 0, -2):
    print(i)