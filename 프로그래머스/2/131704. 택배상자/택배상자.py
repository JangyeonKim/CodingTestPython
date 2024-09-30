def solution(order):
    stack = []
    length = len(order)
    index = 0
    for num in range(1, length + 1):
        stack.append(num)

        while stack and stack[-1] == order[index]:
            stack.pop()
            index += 1

    return index