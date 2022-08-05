# C Specification
# void glFrustum(GLdouble	left,
# 				GLdouble	right,
# 				GLdouble	bottom,
# 				GLdouble	top,
# 				GLdouble	nearVal,
# 				GLdouble	farVal);
# Parameters
# 	left, right
# 	Specify the coordinates for the left and right vertical clipping planes.

# 	bottom, top
# 	Specify the coordinates for the bottom and top horizontal clipping planes.

# 	nearVal, farVal
# 	Specify the distances to the nearer and farther depth clipping planes. These values are negative if the plane is to be behind the viewer.

from sympy import *
init_printing(use_unicode=False, wrap_line=False)
(l, r, b, t, n, f) = symbols('l r b t n f')
# v = Matrix([x, y, z])
A = (r + l)/(r - l)
B = (t + b)/(t - b)
C = -(f + n)/(f - n)
D = -2*f*n/(f - n)

m_view2clip = Matrix([\
						[2*n/(r-l),	0,		   A,		0], \
						[0,	  2*n/(t-b), 	   B, 		0], \
						[0,	  		0,		   C, 		D], \
						[0,	  		0,	       -1, 		0] \
					])

m_clip2view = m_view2clip**(-1)

z_view = m_clip2view*Matrix([0, 0, 1, 0])
z_clip = m_view2clip*Matrix([0, 0, 1, 0])

key_points_view = [\
				Matrix([l, b, -n, 1]),\
				Matrix([r, b, -n, 1]),\
				Matrix([l, t, -n, 1]),\
				Matrix([r, t, -n, 1]),\
				Matrix([0, 0, -n, 1]),\
				]

key_points_clip = []

#for each key point compute the corresponding key point in clip space
for point_view in key_points_view:
	key_points_clip.append(m_view2clip*point_view)

key_points_clip_norm = []
for point_clip in key_points_clip:
	x = point_clip[0]/point_clip[3]
	y = point_clip[1]/point_clip[3]
	z = point_clip[2]/point_clip[3]
	key_points_clip_norm.append(Matrix([x, y, z]))