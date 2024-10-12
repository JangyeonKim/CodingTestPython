def GCD(A, B) :
    a = max(A, B)
    b = min(A, B)
    
    if a % b == 0 :
        return b
    else :
        return GCD(b, a % b)

def arrGCD(array) :
    arr = array.copy()
    while len(arr) > 1 :
        gcd = GCD(arr.pop(), arr.pop())
        if gcd == 1:
            return 1
        arr.append(gcd)
    return arr[0]

def condition(gcd, arr) :
    if gcd == 1:
        return False
    else :
        for a in arr :
            if a % gcd == 0 :
                return False
    return True

def solution(arrayA, arrayB) :
    gcdA = arrGCD(arrayA)
    gcdB = arrGCD(arrayB)
    
    a = gcdA if condition(gcdA, arrayB) else 0
    b = gcdB if condition(gcdB, arrayA) else 0
    
    return max(a, b)