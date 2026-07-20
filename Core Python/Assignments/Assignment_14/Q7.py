#Given two sets of numbers, write a Python program to find the missing
#numbers in the second set as compared to the first and vice versa.
#Use the Python set.
def missinNumber(s1,s2):
    print("Missing in second set:",s1-s2)
    print("Missing in first set:",s2-s1)
s1={1,2,3,7,8}
s2={7,4,5,6,7,8}
missinNumber(s1,s2)

