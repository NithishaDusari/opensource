X=int(input())
def factorial(n):
    r=1
    for i in range(2, n+1):
        r*=i
    return r
A=X*factorial(X-1)
print(A)
