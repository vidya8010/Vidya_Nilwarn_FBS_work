#Write a program to find the second largest element in the list.

def sLargest(li):
    largest = li[0]
    second = li[1]

    for i in range(1, len(li)):
        if li[i] > largest:
            second = largest
            largest = li[i]
        elif li[i] > second:
            second = li[i]
    return largest,second
li = [12,3,4,5,6,7,8]
largest,second=sLargest(li)
print("Largest =", largest)
print("Second Largest =", second)