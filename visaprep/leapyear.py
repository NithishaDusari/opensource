year=int(input().strip())
if 1500<=year<=3000:
    if(year%4==0 and year%100!=0) or (year%400==0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
