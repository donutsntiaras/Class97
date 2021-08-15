mySentence = input("Enter your name and age: ")

wordCount=1

characterCount = 0

for i in mySentence:
    characterCount = characterCount + 1
    if(i == " "):
        wordCount = wordCount + 1                                                     

print("word count is ",wordCount)
print("character count is ",characterCount)
