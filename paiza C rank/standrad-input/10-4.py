H,W,A,B=input().split()
h=int(H)
w=int(W)
for i in range(1,h+1):
    for k in range(1,w+1):
        if k==w:
            print(f"({A}, {B})")
           
            if i<h:
                L=6*w+3*(w-1)
                print("="*L)
                
        
        else:
            print(f"({A}, {B})",end=" | ")
           
  #success     
           
