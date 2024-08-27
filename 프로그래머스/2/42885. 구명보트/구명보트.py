def solution(people, limit):
    people.sort()  # 사람들의 몸무게를 오름차순으로 정렬
    left = 0  # 가장 가벼운 사람을 가리키는 포인터
    right = len(people) - 1  # 가장 무거운 사람을 가리키는 포인터
    boats = 0  # 필요한 구명보트의 수

    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 합이 제한을 넘지 않으면 함께 태운다
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람 태웠으므로 포인터 이동
        # 가장 무거운 사람은 항상 보트에 태운다
        right -= 1  # 가장 무거운 사람 태웠으므로 포인터 이동
        boats += 1  # 보트 하나 사용

    return boats