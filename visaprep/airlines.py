X, N = map(int, input().strip().split())
total_planes_needed=(N+99)//100
additional_planes=max(0,total_planes_needed-X)
print(additional_planes)
