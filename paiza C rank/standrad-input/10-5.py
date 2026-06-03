h,w,a,b=map(int,input().split())
a=str(a).rjust(9," ")
b=str(b).rjust(9," ")
for i in range(h):
    for k in range(w):
        if k==w-1:
            print(f"({a},{b})")
            if i==h-1:
                pass
            else:
                rl=(21*w+3*(w-1))
                print("="*rl)
            
        else:
            print(f"({a},{b})",end=" | ")
#==================================================
h,w,a,b=map(int,input().split())
a=str(a).rjust(9," ")
b=str(b).rjust(9," ")
for i in range(h):
    for k in range(w):
        if k==w-1:
            print(f"({a}, {b})")
            if i==h-1:
                pass
            else:
                rl=(22*w+3*(w-1))
                print("="*rl)
            
        else:
            print(f"({a}, {b})",end=" | ")
#success
            
