import math
a,b,c=map(int,input().split())
s = (a + b + c) / 2
area =(s*(s-a)*(s-b)*(s-c))
ins=math.sqrt(area)
print(format(ins,".2f"))
