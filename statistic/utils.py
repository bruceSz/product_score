def compute_frequency(l):
    length = len(l)
    d = {}
    for i in l:
        if i in d:
            d[i] +=1
        else:
            d[i]  = 1
    r_d = {}
    for k,v in d.iteritems():
        r_d[k] = float(v)/length
    return r_d


def test_c_frequency():
    l = []
    for i in range(20):
        l.append(random.randint(1,10))

    l.sort()
    print l
    d = compute_frequency(l)
    for k,v in d.iteritems():
        print k ,v


if __name__ == "__main__":
    test_c_frequency()