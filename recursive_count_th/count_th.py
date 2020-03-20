'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #Base Case if word is less than or equal to 2 characters
    if len(word) <= 2:
        #If 'th' return 1 else 0
        if word[:2] == 'th':
            return 1
        else:
            return 0
    else:
        #Check one letter at a time moving right on the sting
        if word[0] + word[1] == 'th':
            #Return 1 itterance then move to the next letter with recurssion
            return 1 + count_th(word[1:])
        else:
            #Return 0 itterance then move to the next letter with recurssion
            return 0 + count_th(word[1:])
