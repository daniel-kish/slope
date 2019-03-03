import sys

pts = list()
with open(sys.argv[1]) as f:
	for line in f.readlines():
		# print(line)
		pts.append([float(x) for x in line.split(' ')])

pts.sort(key=lambda x: x[1])

for x in pts:
	print('{{{:03.2f}, {:03.2f}}}'.format(*x))

velocities = []

def fin_dif(p1, p2):
	dfdt = (p2[1] - p1[1])/(p2[0] - p1[0])
	t = (p2[0] + p1[0]) / 2
	return [t, dfdt]

for i in range(0, len(pts)-1):
	velocities.append(fin_dif(pts[i], pts[i+1]))

print('\n')
for x in velocities:
	print('{{{:03.2f}, {:03.2f}}}'.format(*x))

accelerations = []
for i in range(0, len(velocities)-1):
	accelerations.append(fin_dif(velocities[i], velocities[i+1]))

print('\n')
for x in accelerations:
	print('{{{:03.2f}, {:03.2f}}}'.format(*x))

print('\n')

# print for wolfram
def wol_print(lst):
	fmt_str = []
	for el in lst:
		fmt_str.append('{{{:03.4f}, {:03.4f}}}'.format(*el))
	print('{' + ', '.join(fmt_str) + '}')

wol_print(pts)

a_av = 0.0
for x in accelerations: a_av += x[1]

a_av /= len(accelerations)

print('<a> = {}'.format(a_av))

t_full = pts[-1][0] - pts[0][0]
s_full = pts[-1][1] - pts[0][1]
print('a_ov = {}'.format(2.0 * s_full/(t_full*t_full)))

from math import cos, sin, pi

print('\nprediction:\na = {}'.format(9.8*sin(45.0*pi/180.0) - 9.8*0.35*cos(45.0*pi/180.0)))

def correct(l, L, p, y):
	return y - (l/L)*(p-y)

for p in pts:
	print('{:03.4f}, {:03.4f}'.format(p[0],
		  correct(0.005, 0.2, 0.210, p[1])))
