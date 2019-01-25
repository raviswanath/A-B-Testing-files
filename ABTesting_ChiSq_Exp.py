## A/B test experiment to analyze how the convergence rate varies with the number of tests

#importing the needed packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2
from scipy.stats import chi2_contingency

class DataGenerator:

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
	
	def next(self):
		click1 = 1 if (np.random.random() < self.p1) else 0
		click2 = 1 if (np.random.random() < self.p2) else 0
		return click1, click2
		

def get_p_value(T):
	g, p, dof, exptd = stats.chi2_contingency(T, correction = False)
	return p
	
def run_experiment(p1, p2, N):
	data = DataGenerator(p1, p2)
	p_values = np.empty(N)
	T = np.zeros((2,2)).astype(np.float32)
	
	for i in range(N):
		c1, c2 = data.next()
		T[0, c1] +=1
		T[1, c2] +=1
		
		if i < 10:
			p_values[i] = None
		else:
			p_values[i] = get_p_value(T)
	
	plt.plot(p_values)
	plt.plot(np.ones(N)*0.05)
	plt.show()
	
run_experiment(0.1, 0.11, 200000)