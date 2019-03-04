import sys


# print for wolfram
def wol_print(lst):
	fmt_str = []
	for el in lst:
		fmt_str.append('{{{:03.4f}, {:03.4f}}}'.format(*el))
	print('{' + ', '.join(fmt_str) + '}')


pts = list()
with open(sys.argv[1]) as f:
	for line in f.readlines():
		parts = line.split(' ')
		pts.append([float(parts[0]), float(parts[1])])

pts.sort(key=lambda x: x[1])

def fin_dif(p1, p2):
	dfdt = (p2[1] - p1[1])/(p2[0] - p1[0])
	t = (p2[0] + p1[0]) / 2
	return [t, dfdt]

v = []
for i in range(0, len(pts)-1):
	v.append(fin_dif(pts[i], pts[i+1]))

a = []
for i in range(0, len(v)-1):
	a.append(fin_dif(v[i], v[i+1]))

if len(sys.argv) > 2 and sys.argv[2] == '-v':
	print('position:')
	wol_print(pts)
	print('velocity:')
	wol_print(v)
	print('acceleration:')
	wol_print(a)
	print('\n')

a_av = 0.0
for x in a: a_av += x[1]

a_av /= len(a)

print('<a> = {}'.format(a_av))

t_full = pts[-1][0] - pts[0][0]
s_full = pts[-1][1] - pts[0][1]
print('a_ov = {}'.format(2.0 * s_full/(t_full*t_full)))

# from math import cos, sin, pi

# print('\nprediction:\na = {}'.format(9.8*sin(45.0*pi/180.0) - 9.8*0.35*cos(45.0*pi/180.0)))
