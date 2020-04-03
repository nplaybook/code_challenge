# Both players are given the same string,S .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# A player gets +1 point for each occurrence of the substring in the string S.

# Logic: create every possible substrings for each initial character.
# Example: BANANA, for B it will be [B, BA, BAN, BANA, BANAN, BANANAN] for first N it will be [N, NA, NAN, NANA]
# for the second N it will be [N, NA]. Thus, scoring for consonants is 12.

def minion_game(string):
    result = {'Stuart':0, 'Kevin':0}
    
    for i in range(len(string)):
        if string[i] in 'AIUEO':
            result['Kevin'] += (len(string) - i)
        else:
            result['Stuart'] += (len(string) - i)
    
    if result['Kevin'] > result['Stuart']:
        print('Kevin', result['Kevin']) 
    elif result['Stuart'] > result['Kevin']:
        print('Stuart', result['Stuart']) 
    else:
        print('Draw') 

