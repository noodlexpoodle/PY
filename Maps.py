from random import shuffle

def jumble(word):
    #anagram is a list of the characters
    anagram = list(word)
    shuffle(anagram) #shuffle the list
    return ''.join(anagram)
#words = ['apple','pear','melon']
words = []
i = 1
while i == 1:
    word = input('Enter word. Type "Done" to stop ')
    if word.lower() != 'done':
        words.append(word)
    else:
        i = 0
#anagram is the orig list, anagramS is the new empty list for the other list to transform into
anagrams = []

#basic loop method
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

#map function
print(list(map(jumble,words)))

#list comprehension
print([jumble(word) for word in words])
