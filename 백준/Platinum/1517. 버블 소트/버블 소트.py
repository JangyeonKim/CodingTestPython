# 버블 정렬의 시간 복잡도는 n^2 이므로 버블 정렬로 구하게 되면 시간 초과 발생
# nlogn의 시간복잡도를 가지는 병합정렬의 투 포인터 개념 활용해야함

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0

# 재귀적으로 구현
def merge_sort(start, end):
    global answer, arr
    if start < end:
        mid = (start + end) // 2 # 구간 나누기
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        temp = []
        x, y = start, mid + 1 # 투 포인터
        
        while x <= mid and y <= end: 
            if arr[x] <= arr[y]: # 앞쪽 데이터가 더 작은 경우. 즉 swap이 일어나지 않는 경우
                temp.append(arr[x])
                x += 1 # 포인터 증가
            else: # 뒷쪽 데이터가 더 작은 경우. 즉 swap이 일어나는 경우
                temp.append(arr[y])
                y += 1 # 포인터 증가
                answer += (mid - x) + 1 # 앞쪽에 남아있는 데이터 수 만큼의 swap 발생
        
        if x <= mid: # 뒷쪽 데이터를 모두 처리하였는데 앞쪽 데이터가 남아있는 경우에 대한 처리
            temp = temp + arr[x:mid + 1]
        
        if y <= end: # 앞쪽 데이터를 모두 처리하였는데 뒷쪽 데이터가 남아있는 경우에 대한 처리
            temp = temp + arr[y:end + 1]
        
        for i in range(len(temp)):
            arr[start+i] = temp[i]

merge_sort(0, n-1)
print(answer)