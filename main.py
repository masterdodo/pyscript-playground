import math
import numpy as np
import random
from utils import add_class

output_el = Element('output').element

arr = np.array([11, 22, 35, 47, 51, 67, 74, 88])

output_el.innerHTML = f"{arr}"

def shuffle_array(*args):
    shuffled = sorted(arr, key=lambda k: random.random())
    #pyscript.write('output', f"{shuffled}")
    output_el.innerHTML = shuffled
    add_class(output_el, "text-blue-500")