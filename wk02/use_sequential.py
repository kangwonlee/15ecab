# -*- coding: cp949 -*-
import root_finding

def f2(x):
    return float(x*x) - 3.0

print root_finding.sequential(f2, 0.01)

print root_finding.sequential(root_finding.func, 0.01)
