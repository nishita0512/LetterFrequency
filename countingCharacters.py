import matplotlib.pyplot as plt

totalCharCount = 0
charCount = {}

with open('hinglish.txt', 'r', encoding="utf-8") as file:
    char = file.read(1)

    while char:
        if (char>='A' and char<='Z') or (char>='a' and char<='z'):
            totalCharCount+=1
            if char.lower() in charCount:
                charCount[char.lower()]+=1
            else:
                charCount[char.lower()]=1
        char = file.read(1)

print("Number of each characters in the file:", charCount)

for char in charCount.keys():
    charCount[char]*=100
    charCount[char]/=totalCharCount
    charCount[char] = round(charCount[char],2)

print("Percentage of each character in file: ",charCount)

characters = list(charCount.keys())
percentage = list(charCount.values())

plt.bar(range(len(charCount)),percentage,tick_label=characters)
plt.show()