#4. Sum of all odd numbers between 1 to n
def sumOddNumber(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i
    return sum
n=int(input('Enter n:'))
sum=sumOddNumber(n)
print(f'Summation of odd numbers is {sum}')