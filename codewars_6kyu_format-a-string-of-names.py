# input
# an array containing hashes of names
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])

# output
# string formatted as as a list of names separated by commas except for the last two names, 
# which should be separated by an ampersand 
# 'Bart, Lisa & Maggie'

def namelist(names):
    names_string = []
    # access key-value pair
    for name in names:
        # take value
        for value in name.values():
            names_string.append(value)
            
    if len(names_string) <= 1:
        return ''.join(names_string)
    else:
        # add ampersand for the last 2 names
        last_two = ' & '.join(names_string[-2:])
        # add coma 
        rest = [name + ',' for name in names_string[:-2]]
        rest.append(last_two)
        return ' '.join(rest)
