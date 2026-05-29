
n,m=map(int,input().split())
a=int(n*m)
if  n==0 and m==0 :
    print(f"{n} {m}")
elif a==1:
    print(f"{1} {0}")
else:
    print(f"{0} {1}")

#My　answer(success)




a, b = map(int, input().split())

c = a & b
s = a ^ b

print(c, s)

#paiza answer
