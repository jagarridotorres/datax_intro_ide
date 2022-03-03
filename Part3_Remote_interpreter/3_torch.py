
from time import perf_counter
import torch

"""
References (extra examples):
https://github.com/PrincetonUniversity/hpc_beginning_workshop 
https://github.com/PrincetonUniversity/gpu_programming_intro
"""

N = 1000

x = torch.randn(N, N, dtype=torch.float64)
t0 = perf_counter()
u, s, v = torch.svd(x)
elapsed_time = perf_counter() - t0

print("Execution time: ", elapsed_time)
print("Result: ", torch.sum(s).cpu().numpy())
print("PyTorch version: ", torch.__version__)
