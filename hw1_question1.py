def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    counter = 0
    if len(word) < 6:
        return False
    else:
        len_word = len(word)-5
        for ii in range(0,len_word):
            if (word[ii] == word[ii+1]) and (word[ii+2] == word[ii+3]) and (word[ii+4] == word[ii+5]) and word[ii:ii+6].isalpha()==True:
                counter += 1
            else:
                counter = counter
    if counter > 0:
        return True
    else:
        return False

word = '1122aabbcc4'    
print(trifeca(word))
