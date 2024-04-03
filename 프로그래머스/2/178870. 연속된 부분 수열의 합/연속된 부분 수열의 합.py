def solution(sequence, k):
    answer = []
    n=len(sequence)
    i,j=0,0
    a,b=0,0
    l=n
    s=sequence[0]

    while i<n and j<n:
        if j==n-1 and s<k:
            break
        if s>k:
            s-=sequence[i]
            i+=1
        elif s<k:
            j+=1
            s+=sequence[j]
        elif s==k:
            x=j-i
            if x<l:
                l=x
                a=i
                b=j
            if j==n-1:
                break
            j+=1
            s+=sequence[j]

    answer.append(a)
    answer.append(b)


    return answer