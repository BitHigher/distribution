#!/usr/bin/python

import numpy as np
import math
from mayavi import mlab

def ball(xran, zran):
	xa = np.linspace(0, xran, 100)
	za = np.linspace(0, zran, 100)
	xa, za = np.meshgrid(xa, za)

	R = 1
	x = R * np.sin(za) * np.cos(xa)
	y = R * np.sin(za) * np.sin(xa)
	z = R * np.cos(za)

	mlab.mesh(x, y, z)
	mlab.show()

if __name__ == '__main__':
	ball(math.pi*2, math.pi)
