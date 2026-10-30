nf = 1
ns = 1
nr = 0
for i in range(50):
    if i == 0:
        print(nf)
    elif i == 1:
        print(ns)
    else:
        nr = nf + ns
        print(nr)
        nf = ns
        ns = nr