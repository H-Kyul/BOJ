# 답안 2
cnt = 0
for _ in range(int(input())):
    s = input()
    if list(s) == sorted(s, key= s.find):
        cnt += 1
print(cnt)


# 답안 1
def GroupChk(list):
    cnt = 0
    for word in list:
        cnt += 1
        temp = []
        for i in range(len(word)):
            if i==0:
                temp.append(word[i])
            else:
                if (word[i] in temp) & (temp[-1] != word[i]):
                    cnt -= 1
                    break
                temp.append(word[i])
    print(cnt)

N = int(input())

words = []
for _ in range(N):
    words.append(str(input()))

GroupChk(words)
