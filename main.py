import ray
import numpy as np
from Memory import Memory
from Calculator import Calculator
import time
from copy import deepcopy

CALC_NUM = int(1e4)
SHAPE = 1024
ray.init()

def main():
    memory = Memory(100)
    calculators = [Calculator.remote(end=CALC_NUM) for _ in range(3)]
    start = time.time()
    
    #ここで、ray.get([process...])にしてしまうと、calculator.calcとprocessが同時に終了するまで待ってしまい 
    #calculatorのmemが貯まらないため一生終わらない
    mems = mem_loop.remote(memory) 
    calc = [calculator.calc.remote() for calculator in calculators]
    done = ray.wait([mems,*calc])
    print(f"tasks complete:{time.time()-start}s")

@ray.remote
def mem_loop(memory:Memory):
    count = 0
    while count<CALC_NUM:
        mat = np.random.randn(SHAPE,SHAPE)
        vec = np.random.randn(SHAPE)
        memory.add(mat, vec)
        count+=1
    


if __name__=="__main__":
    main()