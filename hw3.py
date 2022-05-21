import operator
d = {'a': 10, 'b': 2, "c": 27, 'e': 30, 'f': 3}
tup_list = list(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(tup_list)
