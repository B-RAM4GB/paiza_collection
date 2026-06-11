s=input()
i,c=input().split()
i=int(i)
print(s[: i - 1] + c + s[i:])

#[:i-1] 0からなので０から何番目か。i-1の後ろを表している
#[i:]   iの前を表している
