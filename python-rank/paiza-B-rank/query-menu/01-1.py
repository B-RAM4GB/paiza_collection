n,k,q=map(int,input().split())

lst=[]
for i in range(n):
    a=input()
    lst.append(a)

lst.insert(k,q)  #リストのinsert()メソッドで、指定した位置に要素を追加（挿入）できる. insert(位置, 要素)

for j in lst:
    print(j)
    
