#Python Program to Sort the List According to the Second Element in Sublist

def useSorted(li,n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if li[j][1] < li[min_index][1]:
                min_index = j

        li[i], li[min_index] = li[min_index], li[i]
lst = [[1, 5], [3, 2], [2, 8], [4, 1]]
n = len(lst)
useSorted(lst,n)
print(lst)