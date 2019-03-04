def part_sum(v, i):
	return sum(v[0:i])

vals = [5.344, 4.09517309249, 3.91929162433, 4.016]

part_sums = []
for i in range(1, len(vals)+1):
	part_sums.append(part_sum(vals, i) / i)

for i in range(0, len(part_sums)-1):
	print(abs(part_sums[i+1] - part_sums[i]))
