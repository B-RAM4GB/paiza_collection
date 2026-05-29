a = int(input())
print(int(not a))   #not 文字　でture/falseが出力。*intをつけると0/1になる

a, b = map(int, input().split())
print(a ^ b)　　　　#文字^文字　でXORができる。　^=XOR *

a,b=map(int,input().split())
print(int(not(a and b)))    #NAND演算(Not AND) *

a,b = map(int, input().split())
print(int(not(a or b)))    #NOR演算(Not OR) *

a,b=map(int,input().split())
print(int(not(a^b)))       #XNOR演算(XOR+Not) *



