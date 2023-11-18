# C Specification
# void glOrtho(	GLdouble	left,
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
# (l, r, b, t, n, f) = symbols('l r b t n f')
(l, r, b, t, n, f) = (0, 1024, 0, 768, -1, 1)
# (l, r, b, t, n, f) = (-1, +1, -1, +1, +1, -1) identity
# (w, h) = symbols('w h')
# (l, r, b, t, n, f) = (0, w, 0, h, +1, -1)

# v = Matrix([x, y, z])
t_x = -(r + l)/(r - l)
t_y = -(t + b)/(t - b)
t_z = -(f + n)/(f - n)

m_view2clip = Matrix([\
						[2/(r-l),	0,		   0,		t_x], \
						[0,	  2/(t-b), 		   0, 		t_y], \
						[0,	  		0,	-2/(f-n), 		t_z], \
						[0,	  		0,	       0, 		1] \
					])

m_clip2view = m_view2clip**(-1)

x_clip = Matrix([1, 0, 0, 0])
y_clip = Matrix([0, 1, 0, 0])
z_clip = Matrix([0, 0, 1, 0])

x_clip_view = m_clip2view*x_clip
y_clip_view = m_clip2view*y_clip
z_clip_view = m_clip2view*z_clip

x_view = Matrix([1, 0, 0, 0])
y_view = Matrix([0, 1, 0, 0])
z_view = Matrix([0, 0, 1, 0])

x_view_clip = m_view2clip*x_view
y_view_clip = m_view2clip*y_view
z_view_clip = m_view2clip*z_view

o_view = Matrix([0, 0, 0, 1]);
o_view_clip = m_view2clip*o_view;

p_far_view = Matrix([0, 0, -1, 1]);
p_far_view_clip = m_view2clip*p_far_view;

p_close_view = Matrix([0, 0, +1, 1]);
p_close_view_clip = m_view2clip*p_close_view;

v_close_view = Matrix([1024/2, 768/2, -0.1, 1])
v_close_clip = m_view2clip*v_close_view

v_far_view = Matrix([1024/2, 768/2, -1.0, 1])
v_far_clip = m_view2clip*v_far_view