

# YOU SHOUL DEPLOY THIS CODE IN GOOGLE COLLAB


# ip install numpy
# pip install imread

#Download image to collab

from google.colab import files
from IPython.display import Image

uploaded = files.upload()

#-------------------  IMAGE INTO MATRIX ----------------------------

import numpy as np
from imread import  imread

img = imread('file_name.jpeg/jpg/png') 


print(img.shape) # -> GET THE FIRST 2 VALUES OF THIS OUTPUT AND REPLACE THE FIRST ONE IN THE "X" LOOP AND THE SECOND ONE IN THE "Y" LOOP 



#--------------- ----------------------------------------

for x in range(0,49):
  for y in range(0,76):
    print(img[x, y])    # THE OUTPUT IS GOINT TO BE EVERY ELEMENT OF THE IMG MATRIX


