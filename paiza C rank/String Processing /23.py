n=input()
s=set()     #空っぽsetを作成し変数sに入れる。setは同じ値を重複して持てない。同じ値が重複すると無視される。
for i in n:
    if i not in s:    #取り出した文字がまだsの中に入っていないのであれば↓
        s.add(i)   
        print(i,end="")
