import os
import folium
from folium import plugins
import pandas as pd
from pandas import Series,DataFrame
import datetime
import json
import math

url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
datas=pd.read_csv(url)

m = folium.Map(
    location=[36.619700,139.728553],
    zoom_start=5
    )
for index,data in datas.iterrows():
    class content():
        def pop():
            if type(data['Province/State'])!=float:
                content=data['Province/State']+' '+data['Country/Region']+':'+str(data[-1])
            else:
                content=data['Country/Region']+':'+str(data[-1])
            return content
        def rad():
            num=data[-1]
            if num>=10000:
                return 70,'red'
            elif 1000<num<10000:
                    return 50,'purple'
            elif 100<num<=1000:
                return 30,'orange'
            else:
                return 10,'yellow'
    folium.CircleMarker(
        location = [data.Lat , data.Long],
        radius=content.rad()[0],
        popup=content.pop(),
        color=content.rad()[1],
        fill=True
    ).add_to(m)
m