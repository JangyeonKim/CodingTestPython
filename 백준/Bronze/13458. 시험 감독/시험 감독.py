N = int(input())

arr = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for a in arr :
    if B >= a : # 총감독 1명으로 가능
        answer += 1
    else :
        answer += 1 # 총감독 1명 할당
        temp = a-B # 총감독 1명 할당하고 남은 응시생
        
        ans = temp // C # 부감독이 몇 명 필요?
        if temp % C == 0 : # 나누어 떨어지면 그대로 더하고, 아니면 +1 해서 더하기
            answer += ans
        else :
            answer += ans+1
            
print(answer)