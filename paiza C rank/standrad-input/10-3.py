
#https://paiza.jp/works/mondai/stdout_primer/stdout_primer__specific_format_step3

for i in range(1,10):
    for k in range(1,10):
        
        N=str(i*k).rjust(2," ")
        
        if i*k==81:
            print(N)
        elif 9==k:
            print(N)
            print("==========================================")
        else:
            print((N),end=" | ")

#success
