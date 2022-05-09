import netCDF4 as nc
import numpy as np
import pandas as pd
import os
import glob
i = 0
for filename in glob.glob('*.nc'): #access all netCDF files in directory
   with open(os.path.join(os.getcwd(), filename), 'r') as f:

    ds = nc.Dataset(filename) #read file

    print(ds)

    saa = ds['solar_azimuth_angle'][:] #read specific value into numpy array

    print(saa)

    df = pd.DataFrame(saa) #create pandas dataframe from numpy array
    df.to_csv('MVIRI{}.txt'.format(i),sep=" ",index=False) #create .txt file with different filename for each iteration

    i+=1