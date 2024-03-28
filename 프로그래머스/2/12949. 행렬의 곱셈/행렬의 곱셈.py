def solution(arr1, arr2):
    
    result_matrix = [] # 최종 결과를 저장할 리스트 초기화
    for row in arr1: # arr1의 각 행에 대해
        temp = [] # 각 행의 결과를 저장할 임시 리스트
        for i in range(len(arr2[0])): # arr2의 각 열에 대해
            sum_result = 0 # 결과값 누적을 위한 변수
            for j in range(len(arr2)): # 곱셈과 누적 과정
                sum_result += row[j] * arr2[j][i]
            temp.append(sum_result) # 누적된 결과를 임시 리스트에 추가
        result_matrix.append(temp) # 임시 리스트를 최종 결과 리스트에 추가
        
    return result_matrix