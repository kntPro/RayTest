import ray
import numpy as np
from Memory import Memory
from tqdm import tqdm
import time

@ray.remote
class Calculator:
    def __init__(self, memlen:int, end:int) -> None:
        self.log = list()
        self.mem = Memory(memlen)
        self.max_calc_num = end
        self.calc_count=0

    def calc(self) -> bool:
        with tqdm(total=self.max_calc_num) as pbar:
            while self.calc_count < self.max_calc_num:
                if self.mem.size() >= 1:
                    mat, vec = self.mem.pop()
                    self.log.append(np.matmul(mat, vec))
                    pbar.update(1)
                    self.calc_count+=1
        return True

    def add(self, mat:np.ndarray, vec:np.ndarray) -> None:
        self.add(mat,vec)

