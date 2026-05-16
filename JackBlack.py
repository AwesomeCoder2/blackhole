import numpy as np 
import matplotlib as mlib

#480 * 270 pixels til visualisering og udregninger.
width = 480
height = 270

px = (x / width) * 2 - 1
py = (y / height) * 2 - 1

ray_dir = np.array([px, py, 1.0])
ray_dir /= np.linalg.norm(ray_dir)

#da black hole
#Vi vil sætte det sorte hul ved koordinaterne (0,0,0) og kameraet ved (0,0,-500) så vi kigger på det sorte hul
