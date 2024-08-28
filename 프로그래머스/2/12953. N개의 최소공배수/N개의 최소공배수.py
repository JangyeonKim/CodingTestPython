def GCD(a, b) :
    if a % b == 0 :
        return b
    else :
        return GCD(b, a%b)

def solution(arr):
    arr.sort()
    
    for i in range(1, len(arr)) :
        gcd = GCD(arr[i], arr[i-1])
        lcm = arr[i] * arr[i-1] / gcd
        arr[i] = lcm
        
    return arr[-1]