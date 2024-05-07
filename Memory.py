import ray
from typing import Optional
from collections import deque
import numpy as np
import random

class Memory:
    def __init__(self,memlen:int|float) -> None:
        self.matmem = deque[np.ndarray](maxlen=memlen)
        self.vecmem = deque[np.ndarray](maxlen=memlen)

    def add(self, mat:np.ndarray, vec:np.ndarray) -> None:
        self.matmem.append(mat)
        self.vecmem.append(vec)

    def size(self) -> int:
        return len(self.matmem), len(self.vecmem)

    def pop(self) -> tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        matmemlen, vecmemlen = self.size()
        if not(matmemlen or vecmemlen):
            return (None,None)
        return self.matmem.popleft(), self.vecmem.popleft

    def sample(self):
        matmemlen, vecmemlen = self.size()
        if not(matmemlen or vecmemlen):
            return (None,None)
        else:
            return random.sample(self.matmem, 1), random.sample(self.vecmem, 1)

    
    