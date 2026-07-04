class Student:
    def __init__(self, name, o, b, s):
        self.name = name
        self.o = o
        self.b = b
        self.s = s

n, k = map(int, input().split())

roster = [None] * n

for i in range(n):
    name, o, b, s = input().split()
    roster[i] = Student(name, o, b, s)

for _ in range(k):
    a, new_name = input().split()
    a = int(a)
    roster[a - 1].name = new_name  #.nameでデータの中からnameを指定してその中身ををnew_nameにおきかえる。


for stu in roster:
    print(stu.name, stu.o, stu.b, stu.s)
