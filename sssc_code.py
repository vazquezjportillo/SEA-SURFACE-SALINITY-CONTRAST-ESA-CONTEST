import netCDF4
import numpy as np
import re
from datetime import datetime
import os



file_names = os.listdir('/home/home/Desktop/DATA/30days/2010')
dates_values = []
maximals = []
minimals = []

for i in range(23):
    file_name = '/home/home/Desktop/DATA/30days/2010'+'/'+file_names[i]
    date = re.search("([0-9]{4}[0-9]{2}[0-9]{2})", file_name)
    date_value = datetime.strptime(date.group(), '%Y%m%d').date()
    dates_values.append(date_value)
    date_string = str(datetime.strptime(date.group(), '%Y%m%d').date())
    date_string = date_string.replace("-","")
    f = netCDF4.Dataset(file_name)
    sss = f.variables['sss'] 
    values_max = []
    values_min = []

    for ii in range(584):
        a = sss[0,ii,:]
        a = list(a)
        values_max.append(max(a))
        values_min.append(min(a))
    
    
    max_value = [v for v in values_max if v != '--']    
    max_value = max(max_value)
    maximals.append(max_value)

    min_value = [v for v in values_min if v != '--']    
    min_value = min(min_value)
    minimals.append(min_value)
    
print(2010)    
    
years = ['2011','2012','2013','2014','2015','2016','2017',
         '2018','2019']    

for j in range(9):
    
    file_names = os.listdir('/home/home/Desktop/DATA/30days/'+years[j])
    
    for k in range(23):
        file_name = '/home/home/Desktop/DATA/30days/'+years[j]+'/'+file_names[k]
        date = re.search("([0-9]{4}[0-9]{2}[0-9]{2})", file_name)
        date_value = datetime.strptime(date.group(), '%Y%m%d').date()
        dates_values.append(date_value)
        date_string = str(datetime.strptime(date.group(), '%Y%m%d').date())
        date_string = date_string.replace("-","")
        f = netCDF4.Dataset(file_name)
        sss = f.variables['sss'] 
        values_max = []
        values_min = []

        for kk in range(584):
            a = sss[0,kk,:]
            a = list(a)
            values_max.append(max(a))
            values_min.append(min(a))
    
    
        max_value = [v for v in values_max if v != '--']    
        max_value = max(max_value)
        maximals.append(max_value)

        min_value = [v for v in values_min if v != '--']    
        min_value = min(min_value)
        minimals.append(min_value)
        
    print(years[j])
    
file_names = os.listdir('/home/home/Desktop/DATA/30days/2020')

for l in range(18):
    file_name = '/home/home/Desktop/DATA/30days/2020'+'/'+file_names[l]
    date = re.search("([0-9]{4}[0-9]{2}[0-9]{2})", file_name)
    date_value = datetime.strptime(date.group(), '%Y%m%d').date()
    dates_values.append(date_value)
    date_string = str(datetime.strptime(date.group(), '%Y%m%d').date())
    date_string = date_string.replace("-","")
    f = netCDF4.Dataset(file_name)
    sss = f.variables['sss'] 
    values_max = []
    values_min = []

    for ll in range(584):
        a = sss[0,ll,:]
        a = list(a)
        values_max.append(max(a))
        values_min.append(min(a))
    
    
    max_value = [v for v in values_max if v != '--']    
    max_value = max(max_value)
    maximals.append(max_value)

    min_value = [v for v in values_min if v != '--']    
    min_value = min(min_value)
    minimals.append(min_value)
        