# You are given  words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word.

# Sample input
# bcdef
# abcdefg
# bcde
# bcdef

# Sample output
# 3
# 2 1 1

# dictionary approach
letters={}
for i in range(int(input())):
    l=input()
    if l not in letters:
        letters[l]=1
    else:
        letters[l]+=1
print(len(letters))
for i in letters:
    print(letters[i],end=" ") 
