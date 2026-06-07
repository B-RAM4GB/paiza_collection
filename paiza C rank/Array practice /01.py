n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
b=a.count(k)    #list/str/tuple.count  aの中からｋと一致する要素の数をカウント
print(b)
