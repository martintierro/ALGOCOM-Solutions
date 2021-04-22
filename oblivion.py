def solve(cards):
    loop = cards[0] + 1
    cards = cards[1:]
    count = 0
    while loop > 0:
        for j in range(len(cards)):
            if cards[j] > 0:
                cards[j] -= 1
                count += 1
        loop -= 1
        if loop > 0:
            count += 1
    return count

cards = list(map(int,input().strip().split(" ")))
print("{}".format(solve(cards)))