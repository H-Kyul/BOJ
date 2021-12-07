def fibonacci(N):
    return f_list[N-1] + f_list[N-2]
f_list = [0,1]
N = int(input())
for i in range(2,N+1):
    f_list.append(fibonacci(i))
print(f_list[N])
