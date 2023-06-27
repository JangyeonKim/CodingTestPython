# 내장 함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

# 람다 표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성

# 일반적인 더하기 함수 정의
def add(a,b) :
  return a+b

print(add(3,7))

# 람다 표현식으로 구현한 더하기 함수
print((lambda a,b : a+b)(3, 7))


# 람다 표현식 예시2

array = [('홍', 50), ('이', 32), ('무', 74)]

def my_key(x) :
  return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key = lambda x : x[1]))