def solution(elements):
    answer = 0
    part_sum = set(elements)
    part_sum.add(sum(elements))
    # print(part_sum)
    
    for i in range(1, len(elements)) :
        temp_arr = elements + elements[:i]
        # print(temp_arr)
        for j in range(len(elements)) :
            temp_sum = sum(temp_arr[j:j+i+1])
            part_sum.add(temp_sum)
    
    return len(part_sum)