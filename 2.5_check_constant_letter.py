sentence = "THis is the testing purpose string."

def is_constant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_constant(i)]
print(consonants)