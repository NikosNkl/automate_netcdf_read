import netCDF4 as nc
import numpy as np
import pandas as pd
import os
import glob
k = 0

for filename in glob.glob('*.nc'): #access all netCDF files in directory
   with open(os.path.join(os.getcwd(), filename), 'r') as f:

    x = []
    y = []
    z = []

    ds = nc.Dataset(filename) #read file

    # print(ds)

    saa = ds['solar_azimuth_angle'][:] #read specific value into numpy array
    print(saa[325][292])
    for j in range(500):
     for i in range(500):
      y.append(j)
      x.append(i)
      z.append(saa[i][j])

    saa = np.column_stack((y, x, z))

    # print(saa)

    df = pd.DataFrame(saa, columns = ['Column','Row','Solar Azimuth Angle']) #create pandas dataframe from numpy array
    df.to_csv('MVIRI{}.txt'.format(k),sep=" ",index=False) #create .txt file with different filename for each iteration

    k+=1