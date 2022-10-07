import psutil
cpu_usage = psutil.cpu_percent().percent
print (cpu_usage)
mem_usage = psutil.virtual_memory().percent
print (mem_usage)
