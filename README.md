# pywrappers
Python package with useful decorators for many tasks.

# timewrappers
* timewrapper - counts time per one call of the function
  Basic usage:

  @timewrapper
  def my_func(a, b):
    return a + b
  
* looptimewrapper - counts average time of function calls
  loops parameter implements how much calls this wrapper should do
  Basic usage:

  @looptimewrapper(loops=1000)
  def my_func(a, b):
    return a + b
