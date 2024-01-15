word = input()

abc_dict = {}

for i in range(ord('a'), ord('z')+1) :
    # abc_dict[chr(i)] = word.find(chr(i))
    print(word.find(chr(i)), end=" ")