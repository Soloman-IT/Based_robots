import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stat






import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import seaborn as sns                           # Seaborn is a library for making statistical graphics in Python
from sklearn.neighbors import KernelDensity

n = 50000
dist_frac = 0.5
x1 = np.random.normal(-10, 2, n)      
x2 = np.random.normal(0, 3, n)   
x = np.concatenate((x1,x2))                      
np.random.shuffle(x)                              
eval_points = np.linspace(np.min(x), np.max(x))  

kde_sk = KernelDensity(bandwidth=1.5, kernel='gaussian')   
kde_sk.fit(x.reshape([-1,1]))                              
y_sk = np.exp(kde_sk.score_samples(eval_points.reshape(-1,1)))  

kde_sp = gaussian_kde(x, bw_method=1.0)   
y_sp = kde_sp.pdf(eval_points)       

plt.plot(eval_points, y_sk)

plt.legend(['График'])
plt.savefig('plot_1.png')


