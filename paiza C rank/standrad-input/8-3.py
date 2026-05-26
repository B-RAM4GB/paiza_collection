le,ri=input().split(".")
ri=ri.ljust(4,"0")   #文字列.ljust(幅,埋める文字) mean:左寄せにして指定した幅になるまで右側を埋める。例:a.ljust(2,"0")→a0
if int (ri[3])==5:
    num=int(ri[:3])+1
else:
    num=int(ri[:3])
ri2=str(num).zfill(3)    #文字列.zfill(桁数)　mean:文字列の左側を 0 で埋めて指定した桁数に揃える. 例:"2".zfill(3)→002

print(le+"."+ri2)

#↑no success

N = float(input())
print("{:.3f}".format(N))

#↑success!(公式答え)

N=float(input())
print(f"{N:.3f}")

#↑success!(my answer)
