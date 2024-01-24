import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

stack = [0] # stack 초기화. stack은 index로 관리
ans = [0 for _ in range(n)]

for i in range(1, n) : # 수열 길이만큼 반복. 0은 stack 초기화할 때 
    if a[stack[-1]] > a[i] : # stack의 top에 있는 index에 해당하는 수열 값이 새로 들어오는 수열 값보다 크면. 즉, 오큰수가 아니면
        stack.append(i) # stack에 index 추가
    else : # 오큰수이면 
        while a[stack[-1]] < a[i] : # stack의 top의 index가 오큰수가 아닐때까지 오큰수 기록
            idx = stack.pop()
            ans[idx] = a[i]
            if not stack : # stack이 비면 while문 탈출
                break
        stack.append(i) # 들어오려는 index 추가
        
# stack에 남아있는 index에 -1처리
for s in stack : 
    ans[s] = -1
    
# 정답 출력

for answer in ans :
    print(answer, end = " ")