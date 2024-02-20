n=int(input())
a=[]
b=[]

for i in range(n):
    x,y=input().split()
    a.append(int(x))
    b.append(int(y))
capacities=[b[0]]
for i in range(1,n):
    cap=capacities[i-1]
    cap=cap-a[i]
    cap=cap+b[i]
    capacities.append(cap)
# print(capacities)
print(max(capacities))
