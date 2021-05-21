import itertools
d ={'2':['a','b','c'], '3':['d','e','f']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
