N = int(input())
k = int(input())
b=2**(k-1)
if (N//b)%2==1:
    print("true")
else:
    print("false")
