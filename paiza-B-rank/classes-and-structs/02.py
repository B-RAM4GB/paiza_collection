n=int(input())
list=[]
for i in range(n):
    n1,o,b,s=input().split()
    list.append([n1,o])   #lループするたびにリストが追加。　1ループ:ist=[1,3]   2ループ目:list=[1,3],[3,5]
age=input()
for k in list:      #リストがなくなるまでループ。回数はリストの数に依存
    name=k[0]
    a=k[1]
    if age==a:
        print(name)
