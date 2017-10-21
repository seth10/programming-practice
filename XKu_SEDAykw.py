import itertools

l = [1, 2, 3, 9]
s = 8

for i,j in itertools.combinations(l, 2):
    if i+j == s:
        print "Yes ({}+{}={})".format(i,j,s)
        break
else:
    print "No"
