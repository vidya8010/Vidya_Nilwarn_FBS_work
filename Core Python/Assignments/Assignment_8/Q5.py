#5. Sum of all prime numbers between 1 to n
def sumOfPrime(n):
    sum=0
    for j in range(2,n+1):
        for i in range(2,j):
            if j%i==0:
                break
        else:
            sum+=j
    print(f'Summation of prime numbers is {sum}')
n=int(input('Enter n:'))
sumOfPrime(n)