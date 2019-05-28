inside_lists = []
score_lists = []
inner_lists = []
for __ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    inside_lists.append([name,score])
    score_lists.append(score)
    #inside_lists.sort(key = lambda x:x[1])

score_list = sorted(list(set(score_lists)))[1]
for a, b in sorted(inside_lists):
    #print a
    if score_list == b:
        print (a)
