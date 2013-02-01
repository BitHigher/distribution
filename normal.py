#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np
import math


def normal(mu, sigma):
	multinormal([(mu, sigma)])

# params: list of (mu, sigma)
def multinormal(params):
	plt.title("Normal Distribution")
	plt.grid()
	
	for (mu, sigma) in params:
		k = 1.0/(pow(2*math.pi, 0.5)*sigma)
		x = np.arange(mu-5, mu+5, 0.2)
		y = [k*pow(math.e, -(xi-mu)**2/(2.0*sigma**2)) for xi in x]
		plt.plot(x, y, label="mu=%f, sigma=%f" % (mu, sigma))

	plt.legend()
	plt.show()

if __name__ == '__main__':
	normal(0, 1)
