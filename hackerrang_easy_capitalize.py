# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.

def solve(s):
    return ' '.join(w.capitalize() for w in s.split(' '))
