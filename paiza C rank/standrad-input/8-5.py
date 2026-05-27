#https://paiza.jp/works/mondai/stdout_primer/stdout_primer__format_real_number_boss

Q=int(input())
for i in range(1,Q+1):
    N,M=input().split()
    N1=float(N)
    M1=int(M)
    print(f"{N1:.{M1}f}")

#success
