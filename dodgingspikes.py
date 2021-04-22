#Jarrett Singian, Jade Tan, Martin Tierro
n = int(input().rstrip())
s = input().rstrip()
answers = [0] * (n + 1)
for position in range(n, 0, -1):
    if position == n:
        answers[position] = 0   
    elif s[position - 1] == "1" or position > n:
        answers[position] = int(1e9)
    elif position + 2 > n:
        answers[position] = answers[position + 1] + 1
    else:
        answers[position] = min(answers[position + 1], answers[position + 2]) + 1
jumps = answers[1]
if jumps >= int(1e9):
    print("-1")
else: 
    print(jumps)