def part_sum(v, i):
	return sum(v[0:i])

vals = [5.344, 4.09517309249, 3.91929162433, 4.016, 5.33324867859]
# vals = [5.95991634919, 4.43063482819, 4.30648319934, 4.52429456631, 4.4]

part_sums = []
for i in range(1, len(vals)+1):
	part_sums.append(part_sum(vals, i) / i)

for i in range(0, len(part_sums)-1):
	print(abs(part_sums[i+1] - part_sums[i]))

print('<a> = {}'.format(part_sums[-1]))
