import ray
import numpy as np
from Memory import Memory
from Calculator import Calculator, CALCULATOR_NUM
import time
from copy import deepcopy

CALC_NUM = int(2**7)
SHAPE = 1024
MEMORY_SIZE = 1024
ray.init()

def main():
    memory = Memory(MEMORY_SIZE)
    calculators = [Calculator.remote(memory=memory, start=128, end=CALC_NUM) for _ in range(CALCULATOR_NUM)]
    start = time.time()
    
    #ここで、ray.get([process...])にしてしまうと、calculator.calcとprocessが同時に終了するまで待ってしまい 
    #calculatorのmemが貯まらないため一生終わらない
    mems = mem_loop.remote(memory) 
    calc = [calculator.calc.remote() for calculator in calculators]
    done = ray.wait([mems,*calc])
    done = [ray.get(obj) for obj in done]
    print(done)
    print(f"tasks complete:{time.time()-start}s")

@ray.remote
def mem_loop(memory:Memory):
    for _ in range(MEMORY_SIZE*2):
        mat = np.random.randn(SHAPE,SHAPE)
        vec = np.random.randn(SHAPE)
        memory.add(mat, vec)
    return True
    


if __name__=="__main__":
    main()