# input format: 
# first line contains the original string, the next line contains the substring

# output format:
# number indicating the total umber of occurences of the substring in the original string

# sample input:
# ABCDCDC
# CDC

# sample output:
# 2

counter = 0
def count_substring(string, sub_string):
    for i in range(0, len(string)-len(sub_string)+1):
        try:   
            if string[i:i+len(sub_string)] == sub_string:
                counter += 1
        except IndexError:
            break
    
    return counter
