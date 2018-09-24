# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:11:45 2018

@author: Jingdong
"""

from geopy.geocoders import Nominatim
import pandas as pd
from googleearthplot import googleearthplot

df=pd.read_excel('Klasseliste 1c 2018_2019.xlsx')
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0')


for i in range(len(df)):
     address ='{0}, {1}'.format(df.loc[i]['Adresse 1'], df.loc[i]['Poststed 1'])
     location = geolocator.geocode(address)
     if location is None:
         print('{} could not find location'.format(address))
     else:
         df.loc[i,'latitude']=location.latitude
         df.loc[i,'longitude']=location.longitude
         df.loc[i,'altitude']=location.altitude
     
     
i=13

lat = df.loc[:,'latitude']
lon = df.loc[:,'longitude'] 

df.loc[i,'latitude']=59.9551678
df.loc[i,'longitude']=10.7597707
df.loc[i,'altitude']=0.0

for i in range(len(df)):
    #for (ilat,ilon) in zip(lat,lon):
    ilat = df.loc[i,'latitude']
    ilon = df.loc[i,'longitude'] 
    location = geolocator.reverse('{0},{1}'.format(ilat,ilon))
    df.loc[i,'Adresse 2']=location.address



#Location(26B, Bergrådveien, Korsvoll, Nordre Aker, Oslo, 0873, Norge, (59.9549259, 10.7583788, 0.0))

""" geopy能使用经纬度距离公式（Vincenty distance） 或球面距离（great-circle distance）公式在两点间计算测地距离 """ 

from geopy.distance import vincenty
address1 = (df.loc[18,'latitude'], df.loc[18,'longitude'])
address2 = (df.loc[3,'latitude'], df.loc[3,'longitude'])
print(float("{0:.2f}".format(vincenty(address1, address2).kilometers)))
   
gep2 = googleearthplot()  
lat = df.loc[:,'latitude']
lon = df.loc[:,'longitude'] 
gep2.PlotLineChart(lat, lon, name="trajectory", color="pink") 
gep2.GenerateKMLFile(filepath="sample3.kml") 

gep3 = googleearthplot()  
lat = df.loc[:,'latitude']
lon = df.loc[:,'longitude'] 
labels=df.loc[:,'label']


for (ilat,ilon,label) in zip(lat,lon,labels):
    gep3.PlotPoints(ilat, ilon,  label)
gep3.GenerateKMLFile(filepath="address2.kml")


gep4 = googleearthplot()  
lat = df.loc[:,'latitude']
lon = df.loc[:,'longitude'] 
labels=df.loc[:,'Navn barn']

for (ilat,ilon,label) in zip(lat,lon,labels):
    gep4.PlotPoints(ilat, ilon,  label)
gep4.GenerateKMLFile(filepath="address.kml")

 
 
