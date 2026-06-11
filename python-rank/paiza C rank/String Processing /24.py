N = int(input())
Q = int(input())
n = [0] * Q　　　　#０をQ個並べたリストを作成
c = [""] * Q

for i in range(Q):
    values = input().split()
    n[i] = int(values[0]) - 1
    c[i] = values[1]

C = input()

ans = [C] * N
for i in range(Q):
    ans[n[i]] = c[i]

print("".join(ans))   #種類.join()    文字列リストを結合。例：",".join([123])であれば1,2,3となる
