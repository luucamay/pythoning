def h_index(n, citations):
    ans = [0]*n
    count = 0
    last_count = 0
    for i in range(n):
        count = score(i, citations, last_count)
        last_count = max(last_count, count)
        ans[i] = last_count
    return ans
def score(x, papers_set, last_count):
    # number of papers on the set with citations at list x
    count = 0
    for i in range(x + 1):
        if papers_set[i] > last_count:
            count += 1
    return count
        

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    arr = [0]*n
    string = raw_input().split(" ")
    for j in xrange(n):
        arr[j] = int(string[j])
    out = h_index(n, arr)
    print "Case #{}: {}".format(i, out)
