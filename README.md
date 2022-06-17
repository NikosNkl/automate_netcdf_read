////[WORK IN PROGRESS] AUTOMATING NETCDF FILES VALUE READING AND EXPORTING IN .TXT FORMAT/////

///DESCRIPTION///

A python script that can be used to automate reading netcdf files and extracting chosen data in form of .txt files. Columns and rows correspond to pixels and in this specific example, the rest of columns are Pressure, Altitude and Temperature for each pixel.
With appropriate adjustments, any value from the netcdf file can be extracted and exported in txt format. If new files are added to the folder, the process will include only those and the previous ones won't be overwritten.

Comments : Further optimization is needed, possibly a GUI can be added too.

///HOW TO USE///

Place the main.py in a folder with netcdf files and execute the code. The .txt files will be created in the same directory.
