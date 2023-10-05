def solution(answers):
    
    # 1 : 1, 2, 3, 4, 5 --> 5개 반복
    # 2 : 2, 1, 2, 3, 2, 4, 2, 5 --> 8개 반복
    # 3 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 --> 10개 반복
    
    ans1 = [[1, 2, 3, 4, 5] * (len(answers)//5 + 1)][0][:len(answers)]
    a1 = [ans1[i]==answers[i] for i in range(len(ans1))]
    a1 = a1.count(True)
    
    ans2 = [[2, 1, 2, 3, 2, 4, 2, 5]  * (len(answers)//8 + 1)][0][:len(answers)]
    a2 = [ans2[i]==answers[i] for i in range(len(ans2))]
    a2 = a2.count(True)
    
    ans3 = [[3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)][0][:len(answers)]
    a3 = [ans3[i]==answers[i] for i in range(len(ans3))]
    a3 = a3.count(True)
    
    ans_list = [[a1,1], [a2, 2], [a3,3]] # 수포자 번호 부여 후 맞춘 갯수 높은 순으로 정렬
    ans_list.sort(key = lambda x : x[0], reverse = True)
    
    answer = [ans_list[0][1]]
    
    for i in range(1,3) :
        if ans_list[i][0] == ans_list[0][0] :
            answer.append(ans_list[i][1])
    
    return answer