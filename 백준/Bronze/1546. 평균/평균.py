N = int(input())

scores = list(map(int, input().split()))
scores.sort()

max_val = scores[-1]

new_score = 0

for i in range(N) :
    new_score += scores[i]/max_val*100
    
print(new_score/N)