import time


def timewrapper(func):
    
    def wrapper(*args,**kwargs):
        time_start = int(round(time.time() * 1000))

        result = func(*args,**kwargs)
        time_stop = int(round(time.time() * 1000))

        
        print(f"Time taken: {time_stop - time_start} millis")
        
    return wrapper
    
    

def looptimewrapper(loops):
    
    def inner(func):
    
        def wrapper(*args,**kwargs):
            benchmarks = []
            
            for i in range(loops):
                time_start = int(round(time.time() * 1000))

                result = func(*args,**kwargs)
        
                time_stop = int(round(time.time() * 1000))

        
                benchmarks.append(time_stop-time_start)
                
            print(f"Average time in {loops} loops: {sum(benchmarks) / len(benchmarks)}")
        
        return wrapper
        
    return inner 
    