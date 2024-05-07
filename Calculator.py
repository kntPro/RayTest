import ray
import numpy as np
from Memory import Memory
from tqdm import tqdm
import time
import torch

@ray.remote
class Calculator:
    def __init__(self, memory:Memory, start:int) -> None:
        self.start_calc_num = start
        self.mem = memory
        self.calc_count=0
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def calc(self) -> bool:
        while self.calc_count <= self.start_calc_num:
            mat, vec = self.mem.sample()
            while bool(mat or vec):
                #torch.matmul(torch.from_numpy(mat).to(device=self.device),torch.from_numpy(vec).to(device=self.device))
                np.matmul(mat,vec)
                mat, vec = self.mem.sample()

            self.calc_count+=1
        return True

    def add(self, mat:np.ndarray, vec:np.ndarray) -> None:
        self.add(mat,vec)

