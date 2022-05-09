import netCDF4 as nc
import numpy as np
import pandas as pd
import os
import glob
i = 0
for filename in glob.glob('*.nc'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:

    ds = nc.Dataset(filename)

    print(ds)

    saa = ds['solar_azimuth_angle'][:]

    print(saa)

    df = pd.DataFrame(saa)
    df.to_csv('MVIRI{}.txt'.format(i),sep=" ",index=False)

    i+=1