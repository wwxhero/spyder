# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:35:22 2022

@author: wangwanxin
"""
from sympy import *
init_printing(use_unicode=False, wrap_line=False)
(left, right, bottom, top, nearval, farval) = symbols('left right bottom top nearval farval')
M = eye(4);
M_prime = eye(4);

# if( pwnd->ogl_ctx.is_ogl )
if True:
    # /*------------------------------------------------------
    # on ogl window flip top and bottom to match OGL_ortho
    # ------------------------------------------------------*/
    x      = top;
    top    = bottom;
    bottom = x;



x   =  2.0 / ( right - left );
y   =  2.0 / ( bottom - top );
z   = -2.0 / ( farval - nearval );
tx  = -( right + left ) / ( right - left );
ty  = -( bottom + top ) / ( bottom - top );
tz  = -( farval + nearval) / ( farval - nearval );

M[ 0, 3 ] = M[ 0, 0 ] * tx + M[ 0, 1 ] * ty + M[ 0, 2 ] * tz + M[0, 3 ]
M[ 1, 3 ] = M[ 1, 0 ] * tx + M[ 1, 1 ] * ty + M[ 1, 2 ] * tz + M[1, 3 ]
M[ 2, 3 ] = M[ 2, 0 ] * tx + M[ 2, 1 ] * ty + M[ 2, 2 ] * tz + M[2, 3 ]
M[ 3, 3 ] = M[ 3, 0 ] * tx + M[ 3, 1 ] * ty + M[ 3, 2 ] * tz + M[3, 3 ]

M[ 0, 0 ] *= x;
M[ 1, 0 ] *= x;
M[ 2, 0 ] *= x;
M[ 3, 0 ] *= x;

M[ 0, 1 ] *= y;
M[ 1, 1 ] *= y;
M[ 2, 1 ] *= y;
M[ 3, 1 ] *= y;

M[ 0, 2 ] *= z;
M[ 1, 2 ] *= z;
M[ 2, 2 ] *= z;
M[ 3, 2 ] *= z;

M_prime = M_prime * Matrix([\
						[x,	0, 0, tx], \
						[0,	y, 0, ty], \
						[0,	0, z, tz], \
						[0,	0, 0, 1] \
					]);

err = M-M_prime