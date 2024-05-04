import ray
import numpy as np
from Memory import Memory
from Calculator import Calculator
import time
from copy import deepcopy

CALC_NUM = int(1e4)
SHAPE = 100
ray.init()

def main():
    calculator = Calculator.remote(memlen=CALC_NUM,end=CALC_NUM)
    start = time.time()
    count = 0
    while count<CALC_NUM:
        mat = np.random.randn(SHAPE,SHAPE)
        vec = np.random.randn(SHAPE)
        calculator.add.remote(mat, vec)
        count+=1
    
    #ここで、ray.get([process...])にしてしまうと、calculator.calcとprocessが同時に終了するまで待ってしまうので
    #calculatorのmemが貯まらないため一生終わらない
    done = ray.wait(calculator.calc.remote())
    print(ray.get(done))
    print(f"tasks complete:{time.time()-start}s")



if __name__=="__main__":
    main()