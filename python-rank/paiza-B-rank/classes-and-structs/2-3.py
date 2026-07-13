class employee:
    def __init__(self, number, name):
        self.number=number
        self.name=name
    def getnum(self):
        return self.number
    def getname(self):
        return self.name
        
n=int(input())
lst=[]

for i in range(n):
    s=input().split()
    cad=s[0]
    
    if cad=="make":
        new_lst=employee(s[1], s[2])
        lst.append(new_lst)
    elif cad=="change_num":
        index=int(s[1])-1
        emp=lst[index]
        
