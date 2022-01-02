import sys
N=int(sys.stdin.readline())
a,b,i=2,7,0
if N==1:
    print(1)
else:
    for i in range(1000000000):
        if a<=N<=b:
            print(i+2)
            break
        else:
            a+=6*(i+1)
            b+=6*(i+2)
