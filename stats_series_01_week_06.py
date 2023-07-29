# Snippet 1: Introduction to Hypothesis Testing
from scipy.stats import ttest_1samp

data = [90, 100, 110, 120, 130]
null_hypothesis_mean = 100
t_stat, p_val = ttest_1samp(data, null_hypothesis_mean)

# Snippet 2: Types of Tests
from scipy.stats import ttest_ind, f_oneway

data1 = [90, 100, 110, 120, 130]
data2 = [95, 105, 115, 125, 135]
t_stat_two_sample, p_val_two_sample = ttest_ind(data1, data2) # Two-Sample t-test
f_stat_anova, p_val_anova = f_oneway(data1, data2) # F-test (ANOVA)

# Snippet 3: Practical Application: A/B Testing
# Simulating A/B Testing for Click-through Rate
import numpy as np

group_a = np.random.binomial(n=1, p=0.10, size=1000)
group_b = np.random.binomial(n=1, p=0.12, size=1000)
t_stat_ab, p_val_ab = ttest_ind(group_a, group_b)
