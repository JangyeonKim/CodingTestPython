def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x: x[1])  # 끝나는 지점을 기준으로 정렬
    camera = routes[0][1]  # 첫 번째 차량의 나가는 지점에 카메라 설치
    
    for r in routes:
        if r[0] > camera:  # 카메라가 해당 경로를 포함하지 않으면
            camera = r[1]  # 새로운 카메라 설치
            answer += 1
    
    return answer
