#!/usr/bin/python

from matplotlib import rc, pyplot as plt
from scipy.special import gamma as Gamma
import numpy as np

rc('text', usetex=True)

def beta(alpha, bet):
	multibeta([(alpha, bet)])

def multibeta(params):
	plt.title("Beta Distribution")
	plt.grid()
	plt.xlabel(r"$x \in [0,1]$")
	x = np.linspace(0, 1, 100)
	for (alpha, bet) in params:
		k = Gamma(alpha+bet)/(Gamma(alpha)*Gamma(bet))
		y = [k*pow(t,alpha-1)*pow((1-t),bet-1) for t in x]
		plt.plot(x, y, label=r"$\alpha=%0.2f, \beta=%0.2f$" % (alpha, bet))

	plt.legend()
	plt.show()

if __name__ == '__main__':
	multibeta([(1,1), (1,2), (1,3), (2,1), (2, 6), (10, 30), (20, 20)])
