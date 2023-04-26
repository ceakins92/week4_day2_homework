words = ['this', 'is', 'a', 'sentence', '.']


words = ['this', 'is', 'a', 'sentence', '.']


def reverse(astring):

    rev_words = [word[::-1] for word in astring.split()]
    astring = " ".join(rev_words)

    return astring


reverse(words)


def reverse2(astring):
    return ' '.join(word[::-1] for word in astring.split(" "))


reverse2(words)
