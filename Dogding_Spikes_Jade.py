n = int(input().rstrip())
s = input().rstrip()
answers = [0] * (n + 1)
INFINITY = int(1e9)

for position in range(n, 0, -1):
    if position == n:
        answers[position] = 0
    elif position > n or s[position - 1] == "1":
        answers[position] = INFINITY
    elif position + 2 > n:
        answers[position] = answers[position + 1] +1
    else:
        answers[position] = min(answers[position + 1], answers[position + 2]) + 1

ans = answers[1]
if ans >= INFINITY:
    print(-1)
else:
    print(ans)