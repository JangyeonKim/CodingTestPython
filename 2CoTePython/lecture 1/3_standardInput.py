# input() : 한 줄의 문자열을 입력받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용

# 예제 : n명의 학생 정보를 입력받아 성적순으로 정렬

n = int(input("학생 수 입력 : "))

data = list(map(int, input("성적 입력 : ").split())) # 입력된 문자열을 공백을 기준으로 분리후 정수형으로 변환, 리스트화

data.sort(reverse = True)

print(data)