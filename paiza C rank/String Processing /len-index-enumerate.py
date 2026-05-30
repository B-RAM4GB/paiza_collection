n=input()
m=int(input())
print(n[m-1])  #m-1番目の文字を出す

s=input()
print(len(s)) #lenで文字列の長さチェック

s=input()
c=input()
print(s.index(c)+1)  #文字列.index(文字列)　は文字列が最初に出てくる位置(０始まり)を返す
 

s = input()
c = input()

for i, ele in enumerate(s):　　　　#enumerateは番号付きでループするための機能　(０始まり)
    if ele == c:
        print(i + 1)

#paiza answer
