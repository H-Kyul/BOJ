from itertools import combinations

N,M = map(int,input().split())
cards = []
ans = 0

while len(cards)!=N:
    cards = list(map(int,input().split()))
for s in list(combinations(cards,3)):
    if (sum(s) <= M) & (sum(s) > ans):
        ans = sum(s)
print(ans)
