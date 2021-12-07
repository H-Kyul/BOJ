N = int(input())
ans = 1666 # max
if N % 5 == 0:
    ans = N//5
else:
    for i in range(N//5,-1,-1):
        if (N-(5*i))%3 == 0:
            ans = i + (N-(5*i))//3
            break
        else:
            ans = -1
print(ans)
