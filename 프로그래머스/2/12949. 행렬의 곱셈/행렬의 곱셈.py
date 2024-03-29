def solution(arr1, arr2):
    
    result_matrix = [] 
    
    for row in arr1 : 
        temp_result = []
        for i in range(len(arr2[0])) : 
            temp = 0
            for j in range(len(arr2)) : 
                temp += row[j] * arr2[j][i]
            temp_result.append(temp)
        result_matrix.append(temp_result)
        
    return result_matrix