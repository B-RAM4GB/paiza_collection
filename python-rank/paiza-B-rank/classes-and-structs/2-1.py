class employee:
    def __init__(self, number, name):
        self.number=number
        self.name=name
        
    def getnum(self):  #selfを使いますよということ。クラスの中でメソッドを作るときはこれを書く
        return self.number
    
    def getname(self):
        return self.name
        
        
lst=[]
        
n=int(input())
for i in range(n):
    s=input()
    S=s.split()
    cad=S[0]
    
    if cad=="make":
        new_lst=employee(S[1], S[2])
        lst.append(new_lst)
        
    elif cad == "getnum":
        index = int(S[1]) - 1  # 何番目か（インデックス）を計算
        emp = lst[index]       # リストから社員を取り出す
        print(emp.getnum())    # その社員の番号を表示する
        
    elif cad == "getname":
        index = int(S[1]) - 1
        emp = lst[index]
        print(emp.getname())   # その社員の名前を表示する
    
