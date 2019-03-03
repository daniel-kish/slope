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
		# print(line)
		pts.append([float(x) for x in line.split(' ')])

pts.sort(key=lambda x: x[1])

velocities = []

def fin_dif(p1, p2):
	dfdt = (p2[1] - p1[1])/(p2[0] - p1[0])
	t = (p2[0] + p1[0]) / 2
	return [t, dfdt]

for i in range(0, len(pts)-1):
	velocities.append(fin_dif(pts[i], pts[i+1]))

accelerations = []
for i in range(0, len(velocities)-1):
	accelerations.append(fin_dif(velocities[i], velocities[i+1]))

print('position:')
wol_print(pts)
print('velocity:')
wol_print(velocities)
print('acceleration:')
wol_print(accelerations)
print('\n')

a_av = 0.0
for x in accelerations: a_av += x[1]

a_av /= len(accelerations)

print('<a> = {}'.format(a_av))

t_full = pts[-1][0] - pts[0][0]
s_full = pts[-1][1] - pts[0][1]
print('a_ov = {}'.format(2.0 * s_full/(t_full*t_full)))

from math import cos, sin, pi

print('\nprediction:\na = {}'.format(9.8*sin(45.0*pi/180.0) - 9.8*0.35*cos(45.0*pi/180.0)))
