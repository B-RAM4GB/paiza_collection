class Student:
    def __int__(self,n1,o,b,s):
        self.n1=n1
        self.o=o
        self.b=b
        self.s=s
        
    def change_name(self,n1):
        self.n1=n1
n,k=[int(x) for x in input().split()]
roster=[None]*n    #中身のないリスト。リストの中に何か入ってないと増やせないので、Noneと書いている。[]と書いても増えない。
for i in range(n):
    n1,o,b,s=input().split()
    roster[i]=Student(n1,o,b,s)
for i in range(k):
    index, new_name=input().split()
    roster[int(index)-1].change_name(new_name)
for student in roster:
    print(student.n1,student.o,student.b,student.s)
    
