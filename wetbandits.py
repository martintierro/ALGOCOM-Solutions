# Jade Tan, Martin Tierro
def solve(n, k, vals):
    answers = [0]*n
    for position in range(n):
        if position == 0:
            answers[position] = vals[position]
        elif position >= k+1:
            answers[position] = max(vals[position] + answers[position - (k+1)], answers[position-1])     
        else:
            answers[position] = max(vals[position], answers[position-1])
    return max(answers)
n, k = list(map(int, input().rstrip().split(" ")))
vals = []
for i in range(n):
    vals.append(int(input().rstrip()))
print("{}".format(solve(n, k, vals)))