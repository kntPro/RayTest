from Memory import *
from Calculator import *
from Parser import *
from util import *


def main():
    if args.compare:
        compare_process(args=args)
    
    ray_memory = RayMemory.remote(args.memory_size)
    calculators = [RayCalculator.remote(memory=ray_memory, args=args) for _ in range(args.calculator_num)]
    start_time = time.time()
    mems = mem_loop.remote(ray_memory) 
    calc = [calculator.calc.remote() for calculator in calculators]
    done = ray.wait([mems,*calc])
    done = [ray.get(obj) for obj in done]
    print(done)
    print(f"tasks complete:{time.time()-start_time}s")

@ray.remote
def mem_loop(memory:Memory):
    for _ in tqdm(range(args.calc_num*2)):
        mat = np.random.randn(args.shape,args.shape)
        vec = np.random.randn(args.shape)
        ray.get(memory.add.remote(mat, vec))
    return True

def compare_process(args:argparse.ArgumentParser) -> None:
    memory = Memory(memlen=args.memory_size)
    calculator = Calculator(memory=memory, args=args)
    start = time.time()
    for _ in tqdm(range(args.calc_num*2)):
        mat = np.random.randn(args.shape,args.shape)
        vec = np.random.randn(args.shape)
        memory.add(mat=mat, vec=vec)
    done = calculator.calc()
    print(done)
    print(f"single tasks complete:{time.time()-start}s")
    
if __name__=="__main__":
    main()