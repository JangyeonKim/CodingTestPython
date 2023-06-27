# 리스트 컴프리 헨션
# 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화

# 예시 1 : 0부터 9까지의 수를 포함하는 리스트
array1 = [a for a in range(10)]
print(array1)

# 예시 2 : 0부터 19까지의 수 중에서 홀수만 포함하는 리스트

array2 = [a for a in range(20) if a%2==1]
print(array2)

# 예시 3 : 1부터 9까지의 수들의 제곱 값을 포함하는 리스트

array3 = [a**2 for a in range(1,10)]
print(array3)