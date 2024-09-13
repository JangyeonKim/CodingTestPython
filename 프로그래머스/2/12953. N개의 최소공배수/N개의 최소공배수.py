def gcd(a, b) :
    if a % b == 0 :
        return b
    else :
        return gcd(b, a%b)
    
def LCM(a,b) : 
    return a * b / gcd(a, b)

def solution(arr):
    lcm = 0
    
    arr.sort(reverse=True)
    
    for i in range(len(arr)-1) :
        lcm = LCM(arr[i], arr[i+1])
        arr[i+1] = lcm
    
    return lcm