#!/usr/bin/python

from mayavi import mlab
from scipy.special import gamma as Gamma
import numpy as np
import math

def dirichlet(a1, a2, a3):
	x = [[t/10.0 for i in range(10)] for t in range(11)]
	y = [[(1-xr[0])/10.0*i for i in range(1,11)] for xr in x]
	x = np.array(x)
	y = np.array(y)

	k = Gamma(a1+a2+a3)/(Gamma(a1)*Gamma(a2)*Gamma(a3))
	z = k*pow(x, a1-1)*pow(y, a2-1)*pow(1-x-y, a3-1)
	for i in range(len(z)):
		for j in range(len(z[i])):
			if np.isinf(z[i][j]):
				z[i][j] = np.nan


	mlab.mesh(x, y, z)
	mlab.show()

if __name__ == '__main__':
	dirichlet(2, 2, 2)
