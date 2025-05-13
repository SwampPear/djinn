import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
def plot_bell_curve(mean=0, std_dev=1):
	data = np.linspace(start=norm.ppf(0.01), stop=norm.ppf(0.99), num=100)
	plt.plot(data, norm.pdf(data, mean, std_dev))
	plt.show()
