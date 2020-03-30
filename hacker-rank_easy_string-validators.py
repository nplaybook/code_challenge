# given a string s and find out if the string s contains alphanumeric, alphabetical characters, digits, lowercase,and
# uppercase characters

# input format
# a single line containing string

# sample input
# qA2

# output format
# True or False for each validator

# sample output
# True
# False
# True
# True
# False


if __name__ == '__main__':
    s = input()

    for validator in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        
        # any takes an iterable action and return True or False value
        print(any(validator(c) for c in s))

