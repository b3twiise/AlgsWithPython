import time

from random import randrange, seed
seed(time.time())

seq = [randrange(10**10)for i in range(100) ]

dd = float("inf")
t1 = time.time()
for x in seq:
	for y in seq:
		if x == y:continue
		d = abs(x-y)
		if d < dd:
			xx, yy, dd = x, y, d
t2 = time.time()

print t2 - t1, "unsorted"
print xx, yy



t1 = time.time()
seq.sort()
for x in seq:
	for y in seq:
		if x == y:continue
		d = abs(x-y)
		if d < dd:
			xx, yy, dd = x, y, d
t2 = time.time()

print t2 - t1, "sorted"
print xx, yy


