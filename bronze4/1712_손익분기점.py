A,B,C = map(int,input().split())
profit = C - B
if profit <= 0:
    print(-1)
else:
    sold = A // profit
    while(True):
        sold += 1
        if sold * profit > A:
            print(sold)
            break
