#given a list of words find all anagrams using a hashmap
testlist =['stop','spot','moon','mono']

def anagrams(testlist):
    anagrams = {}       #dictionary to store anagrams             
    for word in testlist:
        sorted_word = ''.join(sorted(word)) #sort the word 
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return anagrams

print(anagrams(testlist))