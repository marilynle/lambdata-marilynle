

from scipy.stats import sem, t
from numpy import mean

class Confidence_interval:
    ""
    The function calculates the confidence interval
    ""
    def __init__(self, x, ci):
        self.x = x
        self.ci = ci  #  ci = 0.95

    def MME(self):
        self.mean = np.mean(self.x)  #  Sample mean
        self.margin_error = sem(self.x)* t.ppf((1 + self.ci) / 2, len(self.x) - 1)  #  Margin of error


    def ci_endpoints(self):
        LE = self.mean - self.margin_error  #  lower endpoint of ci
        UE = self.mean + self.margin_error  #  Upper endpoint of ci
        return (LE,UE)
