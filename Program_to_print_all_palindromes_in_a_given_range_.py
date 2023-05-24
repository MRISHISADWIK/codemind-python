def palindrome(p):
    s=str(p)
    r=s[::-1]
    ir=int(r)
    if p==ir:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if palindrome(i):
        print(i,end=" ")