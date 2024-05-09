import ray
import time

RAY_DEDUP_LOGS=0

@ray.remote
class PrintClass():
    def __init__(self):
        self.num = 0

    def do(self):
        print(f"{self.num}th call")
        time.sleep(1)
        self.num+=1

@ray.remote
def remote_print(i:int):
    print(f"{i}th call")
    time.sleep(1)

print_class = PrintClass.remote()
start = time.time()
for i in range(5):
    ray.get(print_class.do.remote())
print(f"ray.get total time: {time.time()-start}")

start = time.time()
methods = [print_class.do.remote() for i in range(5)]
ray.wait(methods)
print(f"ray.wait total time: {time.time()-start}")
    