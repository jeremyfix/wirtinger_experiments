# coding: utf-8

"""
Some experiments with complex gradients in torch
"""

import torch
import torch.nn as nn

torch.manual_seed(12345)
dtype = torch.cfloat
l = nn.Linear(2, 1, dtype=dtype)

x = torch.randn(16, 2, dtype=dtype)

#
# First experiment
# Propagate throught the network, compute the complex output
# and apply the backward operation
out = l(x).mean()
l.zero_grad()
out.backward()

lwgrad = l.weight.grad
print(f"Out={out} and dout/dlw*={lwgrad}")
# This prints : Out=(-0.4594990611076355-0.5016348361968994j) and dout/dlw*=tensor([[ 0.1376+0.2357j, -0.1335-0.0466j ]])

#
# Second experiment
# Compute the real part of the output before computing the gradient
l.zero_grad()
out = l(x).mean().real
out.backward()

lwgrad = l.weight.grad
print(f"Out={out} and dout/dlw*={lwgrad}")
# This prints : Out=-0.4594990611076355 and dout/dlw*=tensor([[ 0.1376+0.2357j, -0.1335-0.0466j ]])
