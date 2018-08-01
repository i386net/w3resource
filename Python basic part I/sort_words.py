words = '''
Template strings provide simpler string substitutions as described in PEP 292. 
A primary use case for template strings is for internationalization (i18n) since 
in that context, the simpler syntax and functionality makes it easier to translate
 than other built-in string formatting facilities in Python. 
'''

words = words.split()
wordslen = [(len(word), word)for word in words]

wordslen.sort()
words = ' '.join(w for l, w in wordslen)


print(words)
