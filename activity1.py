def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len (word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("list od words with first and last character same\n", lst)
    return ctr

count= match_words(['abc','cbc','xyz', 'aba', '112341'])
print = match_words("number of words having first and last character same:", count)