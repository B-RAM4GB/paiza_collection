#https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step2

N1,N2=map(int,input().split( ))
for i in range(1,N1+1):
    if i==N1:
        print(i,end="")
    else:
        print(i,end=" ")
print()
for a in range(1,N2+1):
    if a==N2:
        print(a,end="")
    else:
        print(a,end=" ")

#result-success

