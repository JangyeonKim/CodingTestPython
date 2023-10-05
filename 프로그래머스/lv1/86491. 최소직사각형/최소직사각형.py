def solution(sizes):

    arr = [sorted(x) for x in sizes]
    
    garo = 0
    sero = 0
    
    for a in arr :
        if a[0] > garo :
            garo = a[0]
        if a[1] > sero :
            sero = a[1]

    return garo*sero