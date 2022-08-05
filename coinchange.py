#Jarrett Singian, Jade Tan, Martin Tierro
d, q = list(map(int,input().rstrip().split(" ")))
denoms = sorted(list(map(int,input().rstrip().split(" "))))
MAX = 3*int(1e5) 
answers = [[0]*(d) for i in range(MAX+1)]
for curr_v in range(MAX+1):
    for curr_d in range (d):
        if curr_v == 0:
            answers[curr_v][curr_d] = 1
        elif denoms[curr_d] <= curr_v:
            answers[curr_v][curr_d] = answers[curr_v-denoms[curr_d]][curr_d] + answers[curr_v][curr_d-1]
        else:
            answers[curr_v][curr_d] = answers[curr_v][curr_d-1]

ans_list = []
for i in range(q):
    v = int(input().rstrip())
    ans_list.append(answers[v][d-1])
print("{}".format("\n".join(list(map(str,ans_list)))))