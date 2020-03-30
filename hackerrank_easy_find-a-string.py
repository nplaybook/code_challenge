# input format: 
# first line contains the original string, the next line contains the substring

# output format:
# number indicating the total umber of occurences of the substring in the original string

# sample input:
# ABCDCDC
# CDC

# sample output:
# 2

def count_substring(string, sub_string):
    counter = 0
    # define shifting
    for i in range(0, len(string)-len(sub_string)+1):
        try:
            # number of characters to be matched
            if string[i:i+len(sub_string)] == sub_string:
                counter += 1
        except IndexError:
            break
    
    return counter
