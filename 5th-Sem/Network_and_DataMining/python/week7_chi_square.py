"""Week 7: Chi-square test using Python
Usage:
    python week7_chi_square.py
This script performs chi-square test on a sample contingency table and reports statistic and p-value.
"""
import numpy as np
from scipy.stats import chi2_contingency

def main():
    # Example contingency table: rows = [Smoker/Non-smoker], cols = [Disease/NoDisease]
    table = np.array([[90, 60],
                      [60, 110]])
    chi2, p, dof, expected = chi2_contingency(table)
    print("Observed:\n", table)
    print("Expected:\n", expected)
    print(f"Chi-square statistic = {chi2:.4f}, p-value = {p:.6f}, dof = {dof}")
    if p < 0.05:
        print("Reject null hypothesis: variables are likely dependent.")
    else:
        print("Fail to reject null hypothesis: no evidence of dependence.")

if __name__ == '__main__':
    main()
