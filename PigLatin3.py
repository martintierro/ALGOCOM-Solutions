from sys import stdin

vowel = ('a','e','i','o','u','y')
pig = ""
for line in stdin:
    words = line.split()
    for word in words:
        beginning = ""
        index = 0
        if word.startswith(vowel):
            pig = pig + word + "yay "
        else:
            for char in word:
                if char in vowel:
                    end = str(word[index:])
                    break
                else:
                    beginning = beginning + char
                index = index + 1
            pig = pig + (str(end) +  beginning + "ay ")
    pig = pig.strip()
    pig = pig + "\n"
pig = pig.strip()
print(pig)    