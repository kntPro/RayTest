import ray
from typing import Optional
from collections import deque
import numpy as np

class Memory:
    def __init__(self,memlen:int|float) -> None:
        self.matmem = deque[np.ndarray](maxlen=memlen)
        self.vecmem = deque[np.ndarray](maxlen=memlen)

    def add(self, mat:np.ndarray, vec:np.ndarray) -> None:
        self.matmem.append(mat)
        self.vecmem.append(vec)

    def size(self) -> int:
        return len(self.matmem)

    def pop(self) -> tuple[np.ndarray, np.ndarray]:
        return self.matmem.popleft(), self.vecmem.popleft
    
    
