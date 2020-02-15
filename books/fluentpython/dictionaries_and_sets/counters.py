from collections import Counter

ct = Counter('asdlfkjaeorhaasldfalsdfklaheuhasdnaj')
print(ct)

ct.update('aaaaaaaaaaaaaaaa')
print(ct)

print(ct.most_common(3))
