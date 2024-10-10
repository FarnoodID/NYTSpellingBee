import os
# cwd =  os.getcwd()
cwd = os.path.dirname(os.path.abspath(__file__))
cwd = cwd + '\\'
print("Opening file at \'"+cwd+"\'")
with open(cwd+'words.txt','r') as f:
    words = f.readlines()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("Please Enter the letters in a row and center letter at the beginning, like: \"bozinrg\"")
letters=list(input())
center_letter = letters[0]
for letter in letters:
    alphabet.remove(letter)

for i, word in enumerate (words):
    if (i+1 != len(words)):
        words[i] = word[:-1]

tempWords =[]    
for word in words:
    has_other_letters = False
    for letter in alphabet:
        if letter in word:
            has_other_letters = True
            break
    if has_other_letters == False:
        tempWords.append(word)
words = tempWords.copy()

tempWords =[]    
for word in words:
    if center_letter in  word and len(word)>3:
        tempWords.append(word)
words = tempWords.copy()

print("Available words for those letters are:")
counter = 0
for word in words:
    counter +=1 
    print(str(counter)+". "+word)
