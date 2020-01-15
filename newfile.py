import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds = randn(80)
sns.violinplot(ds).get_figure().savefig('violin.png')

#kde has a range of values
sns.violinplot(ds,bw=0.2).get_figure().savefig('violin2.png')