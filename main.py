import netCDF4 as nc
import numpy as np
import pandas as pd
import os
import glob

for data in glob.glob('*.nc'): #access all netCDF files in directory
   s = os.path.join(os.getcwd(), data)
   with open(s, 'r') as fn:

    s = (os.path.basename(s))

    s = os.path.splitext(s) #same filename for exported .txt

    print (s[0])

    x = []
    y = []
    z = []
    a = []
    b = []

    ds = nc.Dataset(data) #read file
    print(ds)

    print(ds['ny'])

    press = ds['ctth_pres'][:] #read specific value into numpy array
    alti = ds['ctth_alti'][:]
    temp = ds['ctth_tempe'][:]
    leny = ((ds['ny']).shape[0])
    lenx = ((ds['nx']).shape[0])
    # print(leny)
    # print(press[273][2582])
    # print(press)
    for j in range(leny):
     for i in range(lenx):
      y.append(j)
      x.append(i)
      z.append(press[j][i])
      a.append(alti[j][i])
      b.append(temp[j][i])

    final = np.column_stack((y, x, z, a, b))

    df = pd.DataFrame(final, columns = ['Column','Row','Pressure','Altitude','Temperature']) #create pandas dataframe from numpy array
    df.to_csv('{}.txt'.format(s[0]),sep=" ",index=False) #create .txt file with different filename for each iteration