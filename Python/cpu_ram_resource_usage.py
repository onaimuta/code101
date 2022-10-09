import psutil
cpu_usage = psutil.cpu_percent().percent
print (cpu_usage)
mem_usage = psutil.virtual_memory().percent
print (mem_usage)

from tqdm import tqdm
from time import sleep
import psutil

# cpu_usage = psutil.cpu_percent()
# print (cpu_usage)
# mem_usage = psutil.virtual_memory()
# print (mem_usage)

with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
    while True:
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        rambar.refresh()
        cpubar.refresh()
        sleep(0.5)
