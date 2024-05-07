import ray
import numpy as np
from Memory import Memory
from tqdm import tqdm
import time
import torch

CALCULATOR_NUM=3

@ray.remote
class Calculator:
    def __init__(self, memory:Memory, start:int, end:int) -> None:
        self.start_calc_num = start
        self.end_calc_num = end
        self.mem = memory
        self.calc_count=0
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def calc(self) -> bool:
        while self.calc_count < self.end_calc_num:
            if self.calc_count <= self.start_calc_num:
                continue
            mat, vec = self.mem.sample()
            try:
                assert mat or vec, f"mat was {mat},   vec was {vec}"
            except AssertionError as err:
                print(f"Calculator have not been able to sample from memory \n {err}")
            #torch.matmul(torch.from_numpy(mat).to(device=self.device),torch.from_numpy(vec).to(device=self.device))
            np.matmul(mat,vec)
            self.calc_count+=1
        return True

    def add(self, mat:np.ndarray, vec:np.ndarray) -> None:
        self.add(mat,vec)

