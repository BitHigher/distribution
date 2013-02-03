#!/usr/bin/python

from matplotlib import rc, pyplot as plt
import numpy as np
from scipy.special import gamma as Gamma
import math

rc('text', usetex=True)

def gamma(alpha, beta):
	multigamma([(alpha, beta)])

def multigamma(params):
	plt.title("Gamma Distribution")
	plt.grid()

	x = np.arange(0.1, 20, 0.25)
	for (alpha, beta) in params:
		ga = Gamma(alpha)
		ba = pow(beta, alpha)
		y = [ba*pow(t,alpha-1)*pow(math.e, -beta*t)/ga for t in x]
		plt.plot(x,y, label=r'$\alpha=%0.2f, \beta=%0.2f$' % (alpha, beta))

	plt.legend()
	plt.show()
	#plt.savefig("test.png")


if __name__ == '__main__':
#	gamma(1, 0.5)
	multigamma([(1,0.5), (2,0.5), (3,0.5), (2,1), (2,0.2)])
