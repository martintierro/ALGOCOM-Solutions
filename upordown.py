def solve(n, m, valence):
    MOD = 1000000007
    answers = [[0]*(m+1) for i in range(n+2)]
    for position in range(n+2):
        for p_val in range(m+1):
            if position == 0:
                answers[position][p_val] = 1
            elif valence[position-1] == "1":
                for j in range(p_val-1):
                    answers[position][p_val] += answers[position-1][j]
            elif valence[position-1] == "0":
                for j in range(p_val+1, m+1):
                    answers[position][p_val] += answers[position-1][j]
            elif valence[position-1] == "-":
                answers[position][p_val] = answers[position-1][p_val]
    return sum(answers[n+1])


n, m = list(map(int, input().rstrip().split(" ")))
valence = input().rstrip()
print("{}".format(solve(n, m, valence)))
