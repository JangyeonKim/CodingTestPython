def solution(clothes):
    c_dict = dict()
    
    for item, cate in clothes :
        if cate not in c_dict.keys() :
            c_dict[cate] = [item]
        else :
            c_dict[cate].append(item)
            
    item_list = [len(v)+1 for v in c_dict.values()]
    answer = 1
    for i in item_list :
        answer *= i 
    
    return answer - 1