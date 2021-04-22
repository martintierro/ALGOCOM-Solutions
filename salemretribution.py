# Jarrett Singian, Jade Tan, Martin Tierro
def solve(L, n, coverage):
    old_s = new_s = 1
    old_e = new_e = L
    count = len(coverage)
    coverage.sort()
    reversed_coverage = sorted(coverage, key=lambda x: x[1], reverse=True)
    while(new_s <= new_e):
        if len(coverage) == 0 or coverage[0][0] > new_s or reversed_coverage[0][1] < new_e:
            return "'Salem's Lot is doomed."
        filter_s = [i for i in coverage if i[0] >= old_s and i[0] <= new_s]
        filter_e = [i for i in coverage if i[1] <= old_e and i[1] >= new_e]
        max_s = max(map(max, filter_s))  # get highest left bound
        max_e = min(map(min, filter_e))  # get highest right bound
        if max_s >= new_e or max_e <= new_s:
            count -= 1
            return count
        elif max_s >= max_e - 1:
            count -= 2
            return count
        else:
            count -= 2
            old_s = new_s
            old_e = new_e
            new_s = max_s + 1
            new_e = max_e - 1
            coverage = [i for i in coverage if i[0] > old_s and i[1] < old_e]
            coverage.sort()
            reversed_coverage = sorted(
                coverage, key=lambda x: x[1], reverse=True)
    return count


L, n = list(map(int, input().rstrip().split(" ")))
coverage = [list(map(int, input().rstrip().split(" "))) for i in range(n)]
print(solve(L, n, coverage))
