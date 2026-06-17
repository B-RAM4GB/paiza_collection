n=int(input())
list_n=[]
for i in range(n):
    n1,o,b,s=input().split()
    list_n.append([n1,int(o),b,s])  #
list_n.sort(key=lambda x: x[1])   #sort(デフォルトでは小さい順)はkeyに従ってリストの中身を並び替えてくれる。lambda x: x[1]はリストの一番目の要素を取り出す関数。
for k in list_n:                  #もし大きい順にしたいのであれば(key=lambda x: x[1], reverse=True)とする。
    print(k [0], k[1], k[2], k[3])
        
