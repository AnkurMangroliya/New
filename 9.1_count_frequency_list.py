def count_word_frequency(words):
    d ={}
    for i in range(len(words)):
        if words[i] in d:
            d[words[i]] = d[words[i]]+1
        else:
            d[words[i]]=1
    return d

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))

def count_word_frequency(words):
    d ={}
    for word in words:
        d[word] = d.get(word,0) + 1
    return d


from collections import Counter
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(Counter(words))
