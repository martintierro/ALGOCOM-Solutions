def ispangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    missing = ''
    for char in alphabet:
        if char not in str.lower():
            missing += char
    return missing

num = int(input())
Inputs = []
for i in range(num):
    Inputs.append(input())

for string in Inputs:
    result = ispangram(string)
    if result == '':
        print('pangram')
    else:
        print('missing ' + result)
