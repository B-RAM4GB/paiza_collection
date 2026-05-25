#https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step4

N=int(input())

M=input().split()

for i in range(N):
    M2=int(M[i])+1
    for k in range(1,M2):
        if k==M2-1:
            print(k)
        else:
            print(k,end=" ")
#success
