n,k=map(int,input().split())

lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)
    
if k in lst:      ## リスト「lst」の中に「k」があるか判定する
    print("YES")
else:
    print("NO")
