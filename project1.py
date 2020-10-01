#Bottle Neck Problem Solution
n=int(input())
l=list(map(int, input().split()))
x=[]
for i in l:
    x.append(l.count(i))
print(max(x))
