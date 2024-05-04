import ray
import numpy as np
from Memory import Memory
from tqdm import tqdm
import time
import torch

@ray.remote(num_gpus=0.5)
class Calculator:
    def __init__(self, end:int) -> None:
        self.max_calc_num = end
        self.calc_count=0
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def calc(self) -> bool:
        with tqdm(total=self.max_calc_num) as pbar:
            while self.calc_count < self.max_calc_num:
                try:
                    mat, vec = self.mem.pop()
                except:
                    continue
                #torch.matmul(torch.from_numpy(mat).to(device=self.device),torch.from_numpy(vec).to(device=self.device))
                np.matmul(mat,vec)
                pbar.update(1)
                self.calc_count+=1
        return True

    def add(self, mat:np.ndarray, vec:np.ndarray) -> None:
        self.add(mat,vec)

