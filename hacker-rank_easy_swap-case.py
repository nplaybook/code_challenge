# input format
# a single line containing a string s

# input example
# HackerRank.com presents "Pythonist 2".

# output format
# print modified string s

# output example
# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    update_s = ""
    for c in s:
        if c.islower() == True:
            update_s += c.upper()
        else:
            update_s += c.lower()
    return update_s
