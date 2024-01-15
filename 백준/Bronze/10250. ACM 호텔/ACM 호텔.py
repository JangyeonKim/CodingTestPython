case = int(input())

for _ in range(case) :
    h, w, n = map(int, input().split())
    room_num = []
    for ww in range(1, w+1) :
        for hh in range(1, h+1) :
            if ww < 10 :
                room_num.append(str(hh) + "0" +str(ww))
            else :
                room_num.append(str(hh) + str(ww))
    
    print(int(room_num[n-1]))