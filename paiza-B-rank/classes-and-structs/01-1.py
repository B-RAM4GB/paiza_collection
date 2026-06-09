n=int(input())
for i in range(n):
    n1,o,b,s=input().split()
    print("User{")               #f"user{}"はf"{}"と同じ意味になってしまうので別出力
    print(f"""nickname : {n1}
old : {o}
birth : {b}
state : {s}""")
    print("}")
