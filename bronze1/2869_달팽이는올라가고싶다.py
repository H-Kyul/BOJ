UP,DOWN,TOP = map(int,input().split())
# 초기 설정
day = (TOP // (UP-DOWN)) - UP
h = day * (UP-DOWN)
if day < 0 or h < 0:
    day,h = 0,0
    
while(True):
    day += 1
    if h + UP >= TOP:
        print(day)
        break
    else:
        h += (UP-DOWN)
