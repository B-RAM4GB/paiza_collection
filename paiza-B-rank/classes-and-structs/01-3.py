n=int(input())
list_n=[]
for i in range(n):
    n1,o,b,s=input().split()
    list_n.append([n1,int(o),b,s])
list_n.sort(key=lambda x: x[1])   #sortはリストの中身を並び替えてくれる。
for k in list_n:
    print(k [0], k[1], k[2], k[3])
        
