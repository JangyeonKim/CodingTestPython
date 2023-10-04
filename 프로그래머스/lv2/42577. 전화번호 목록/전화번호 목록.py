def solution(phone_book):
    # for i in range(len(phone_book)) :
    #     for j in range(len(phone_book)) :
    #         if i == j :
    #             pass
    #         else :
    #             if phone_book[i] in phone_book[j][:len(phone_book)] :
    #                 return False
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1) :
        if phone_book[i+1].startswith(phone_book[i]) :
            return False
    
    return True