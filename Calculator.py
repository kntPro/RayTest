import ray
import numpy as np
from Memory import *
from tqdm import tqdm
import time
import torch
import argparse


class Calculator:
    def __init__(self, memory:Memory, args = argparse.ArgumentParser) -> None:
        self.end_calc_num = args.calc_num
        self.mem = memory
        self.calc_count=0
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def calc(self) -> bool:
        while self.calc_count < self.end_calc_num:
            matlen, veclen = self.mem.size()
            if matlen==0 or veclen==0:
                continue
            mat, vec = self.mem.sample()
            #torch.matmul(torch.from_numpy(mat).to(device=self.device),torch.from_numpy(vec).to(device=self.device))
            np.matmul(mat,vec)
            self.calc_count+=1
        return True


@ray.remote
class RayCalculator(Calculator):
    def __init__(self, memory, args=argparse.ArgumentParser) -> None:
        super().__init__(memory, args)

    def calc(self) -> bool:
        while self.calc_count < self.end_calc_num:
            matlen, veclen = ray.get(self.mem.size.remote())
            if matlen==0 or veclen==0:
                continue
            mat, vec = ray.get(self.mem.sample.remote())
            #torch.matmul(torch.from_numpy(mat).to(device=self.device),torch.from_numpy(vec).to(device=self.device))
            np.matmul(mat,vec)
            self.calc_count+=1
        return True
