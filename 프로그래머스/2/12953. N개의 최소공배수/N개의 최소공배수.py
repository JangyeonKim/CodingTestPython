def gcd(a,b) :
    mod_a = a%b
    
    if mod_a == 0 :
        return b
    else :
        return gcd(b, mod_a)

def LCM(a,b,g) :
    return int(a*b/g)
    
def solution(arr):
    arr.sort(reverse=True)
    arr1, arr2 = arr[:2], arr[2:]
    init_lcm = LCM(arr1[0], arr1[1], gcd(arr1[0],arr1[1]))

    lcm = init_lcm
    for i in arr2 :
        lcm = LCM(lcm, i, gcd(lcm,i))
    
    return lcm