from typing import Any, Callable, Tuple
from concurrent.futures import ThreadPoolExecutor

def run_parallel(*funcs: Callable[[], Any]) -> Tuple[Any, ...]:    
    max_workers = min(len(funcs), 3)    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:        
        print("Starting parallel execution (%s workers)", max_workers)        
        func_futures = [executor.submit(f) for f in funcs]        
        return tuple(fut.result() for fut in func_futures)
    
def f1():
    return 1

def f2():
    return 2

funcs = [f1, f2]
print(run_parallel(*funcs))
# (1, 2)


# class A:
#     func a(param1, param2)
#     func a(param1)




